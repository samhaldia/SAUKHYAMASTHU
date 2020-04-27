# coding: utf-8
from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, ValidationError
import atexit
import os
import json
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import requests
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

app = Flask(__name__, static_url_path='')
GoogleMaps(app, key="AIzaSyCLiazO04XQ83QPAA9YDAhpgduggM1tqLY")
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
db_name = 'mydb'
client = None
db = None

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif "CLOUDANT_URL" in os.environ:
    client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'], url=os.environ['CLOUDANT_URL'], connect=True)
    db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8080))

@app.route('/')
def root():
    return render_template('home.html')
	
	
class SelfReportingForm(Form):
    #name = StringField('NAME', validators=[Required()])
    #submit = SubmitField('Submit')
    name = TextField("Name",  [validators.Required()])
    email = TextField("Email",  [validators.Required(), validators.Email()])
    subject = TextField("Subject",  [validators.Required()])
    message = TextAreaField("Message",  [validators.Required()])
    phone = StringField('Phone', [validators.Required()])
    submit = SubmitField("Send")
	
	
    @app.route('/self-reporting', methods=['GET', 'POST'])
    def self_reporting():
        form = SelfReportingForm(request.form)			
        print (form.errors)
        if request.method == 'POST':
            name=request.form['name']
            email=request.form['email']
            subject=request.form['subject']
            message=request.form['message']
            lat= request.form['lat']
            long= request.form['long']
            city= request.form['city']
            state= request.form['state']
            phone=request.form['phone']
            data = {'name':name, 'email':email, 'phone': phone, 'subject': subject, 'message':message, 'lat':lat, 'long':long, 'city':city, 'state':state}
            if client:
                my_document = db.create_document(data)
                print('Doc created in db')
            print (name)
            
            #return render_template('self-reporting-form.html')
            if form.validate() == False:
                flash('All fields are required.')
                return render_template('self-reporting-form.html', form=form)
            else:
                flash("Message Received, We will get back to you soon", 'success')
                return render_template('self-reporting-form.html', form=form)
 
        elif request.method == 'GET':
            return render_template('self-reporting-form.html', form=form)
    

@app.route("/reports")
def mapview():
    # creating a map in the view
    email=''
    lat=0
    long=0
    subject=''
    loclist=[]
	
    if client:
        #print(list(map(lambda doc: doc['name'], db)))
        result_collection = Result(db.all_docs, include_docs=True)
        #print(result_collection[0])
        
        for i in result_collection:
            print(i['doc'])
            for j in i['doc']:
                print(i['doc'][j])
                loclist.append(tuple((i['doc']['lat'],i['doc']['long'])))
        
    
    circle = { # draw circle on map (user_location as center)
        'stroke_color': '#0000FF',
        'stroke_opacity': .5,
        'stroke_weight': 5,
        # line(stroke) style
        'fill_color': '#FFFFFF', 
        'fill_opacity': .2,
        # fill style
        'center': { # set circle to user_location
            'lat': 25.5908,
            'lng': 85.1348
        }, 
        'radius': 20000 # circle size (50 meters)
    }
    mymap = Map(
        identifier="selfreportedmap",
        lat=22,
        lng=77,
		language="en",
		region="IN",
		zoom=16,
		style="height:300px;width:800px;margin:0;",
		fit_markers_to_bounds = True,
        markers=[{'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
                'lat':  i['doc']['lat'],
                'lng':  i['doc']['long'],
                "infobox": "<b><i>Email: "+i['doc']['email']+"</i></b>"+"<br/>"+"<b><i>Phone: "+i['doc']['phone']+"</i></b>"+"<br/>"+"<b><i>Subject: "+i['doc']['subject']+"</i></b>"+"<br/>"+"<b><i>Message: "+i['doc']['message']+"</i></b>"+"<br/>"+"<b><i>State: "+i['doc']['state']+"</i></b>"+"<br/>"+"<b><i>City: "+i['doc']['city']+"</i></b>"} for i in result_collection for j in i['doc']],
        circles = [circle] # pass circles

    )
    return render_template('reports.html', mymap=mymap)	
	
	
@app.route('/info')
def covid_info():
    return render_template('info.html')

# /* Endpoint to greet and add a new visitor to database.
# * Send a POST request to localhost:8000/api/visitors with body
# * {
# *     "name": "Bob"
# * }
# */
@app.route('/api/visitors', methods=['GET'])
def get_visitor():
    if client:
        return jsonify(list(map(lambda doc: doc['name'], db)))
    else:
        print('No database')
        return jsonify([])

# /**
#  * Endpoint to get a JSON array of all the visitors in the database
#  * REST API example:
#  * <code>
#  * GET http://localhost:8000/api/visitors
#  * </code>
#  *
#  * Response:
#  * [ "Bob", "Jane" ]
#  * @return An array of all the visitor names
#  */
@app.route('/api/visitors', methods=['POST'])
def put_visitor():
    user = request.json['name']
    data = {'name':user}
    if client:
        my_document = db.create_document(data)
        data['_id'] = my_document['_id']
        return jsonify(data)
    else:
        print('No database')
        return jsonify(data)

@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=port, debug=True)
