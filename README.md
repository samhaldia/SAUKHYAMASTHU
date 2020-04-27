# SAUKHYAMASTHU


## Contents

1. [Short description](#short-description)
1. [Demo video](#demo-video)
1. [The architecture](#the-architecture)
1. [Long description](#long-description)
1. [Getting started](#getting-started)
1. [Live demo](#live-demo)
1. [Authors](#authors)
1. [License](#license)


## Short description

SAUKHYAMASTHU facilitates a citizen to get in touch with the concerned authorities at the time of a pandemic, calamity or trouble

### What's the problem?

COVID-19 is spreading by leaps and bounds, in such chaotic situaion its not only duty of govt. body, every individual need to join the hand put a simple effort.

### How can technology help?

Every Indiviaduls could be the part of global combat in times of pandemic

### The idea

A Inclusive Web Platform to make evry Individual a Warrior in times of Pandemic by self-reporting and registering the Pandemic Incidents, Frauds, and Rule Violation, or leveraging help to needy, provide info of migrations inter state or nation, Schools with computer facility, Medic Centres and many more. It will also help administrators and decision makers in getting proper visualozation and Insights to take apt action in right direction and guide the people to right direction.

## Demo video

[![Watch the video](https://github.com/samhaldia/SAUKHYAMASTHU/blob/master/Video-Caption.JPG?raw=true)](https://youtu.be/EHR7A5d9TSg)

## The architecture

![Roadmap](https://github.com/samhaldia/SAUKHYAMASTHU/blob/master/architecture.JPG?raw=true)


1. The user navigates to the portal and has access to its services: Self-Reporting, Insights from Reporting, COVID-19 Information, etc.
2. The Web app stores the info collected from user as document within IBM Cloudant NoSQL storage.
3. IBM Watson usage for Data Refinery, Chabot, and any other services to leverage the solution.
4. External Services like Google Map to locate and point out Users, Government Data Services, etc.


## Long description

The entire mankind is facing the life threatening problem due to the COVID 19 pandemic.  With no medicine to cure COVID 19, all the nations have adopted the ‘lockdown’ to curb the pandemic. 
With the help of technology, any citizen can contribute through their own initiative to support the efforts of the Government.  Such initiatives can be like – reporting health related incidents in their locality, symptoms of illness and raising alarm, movement of new persons with migration history, raising the concerns of black marketing of ration items, creating awareness about the fraud emails or cyber crimes during the lockdown period, misleading or fake videos etc.  Such initiatives by citizens can draw the attention of the concerned authorities for taking prompt remedial action.  
The solution Saukhyamasthu can be adopted in any similar situation or in any geographical location or time. 



## Getting started

git clone https://github.com/samhaldia/SAUKHYAMASTHU.git to download the repo

### Prerequisites


You'll need the following:
* [IBM Cloud account](https://console.ng.bluemix.net/registration/)
* [Cloud Foundry CLI](https://github.com/cloudfoundry/cli#downloads)
* [Git](https://git-scm.com/downloads)
* [Python](https://www.python.org/downloads/)
* [Docker] (https://docs.docker.com/get-docker/)

2. Put all the packages in requirements.txt as below
 
Flask>=1.0.0
cloudant==2.4.0
flask-bootstrap>=3.3.7.0
Flask-WTF>=0.14.1
email-validator>=1.0.5
flask-googlemaps>=0.4.0


### Installing

A step by step series of examples that tell you how to get a development env running

Install the dependencies listed in the [requirements.txt](https://pip.readthedocs.io/en/stable/user_guide/#requirements-files) file to be able to run the app locally.

You can optionally use a [virtual environment](https://packaging.python.org/installing/#creating-and-using-virtual-environments) to avoid having these dependencies clash with those of other Python projects or your operating system.

  ```
pip install -r requirements.txt
  ```

Update the vcap-local.json according to your credentials

Update the manifest.yml with your app name

Run the app.
  ```
python hello.py
  ```


## Live demo
https://ucare-quick-gorilla.eu-gb.mybluemix.net/self-reporting


## Authors

* **Sameer Kumar Choudhary** 
* **Krishna Priya tadepalli**
* **Saravjeet Lamba**


## License

This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details