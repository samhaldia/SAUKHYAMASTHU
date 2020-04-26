jQuery(document).ready(function(e) {

	//fontSize increase & decrease start
	if (_getCookie("fontSize") != null) {
		var fontSize = _getCookie("fontSize");
		jQuery("#main-content").css("font-size", fontSize + "px");
	
	} else {
		var fs = jQuery("body").css('font-size');
		var fontSize = fs;
		jQuery("#main-content").css("font-size", fs);	
	}	
	
	function _set_font_size(fontType) {
	
		if (fontType == 'increase') {
	
			if (parseInt(fontSize) < 18) {
	
				fontSize = parseInt(fontSize) + 2;
			}
		} else if (fontType == "decrease") {
			if (parseInt(fontSize) > 10) {
				fontSize = parseInt(fontSize) - 2;
			}
		} else {
			fontSize = 14;
		}
		_setCookie("fontSize", fontSize);
		jQuery("#main-content").css("font-size", fontSize + "px");
	}
	
	// cookies	
	function _getCookie(name) {
		var arg = name + "=";
		var alen = arg.length;
		var clen = document.cookie.length;
		var i = 0;
		while (i < clen) {
			var j = i + alen;
			if (document.cookie.substring(i, j) == arg) {
				return _getCookieVal(j);
			}
			i = document.cookie.indexOf(" ", i) + 1;
			if (i == 0)
				break;
		}
		return null;
	}
	
	function _deleteCookie(name, path, domain) {
		if (_getCookie(name)) {
			document.cookie = name + "=" +
				((path) ? "; path=" + path : "") +
				((domain) ? "; domain=" + domain : "") +
				"; expires=Thu, 01-Jan-70 00:00:01 GMT";
		}
	}
	
	function _setCookie(name, value, expires, path, domain, secure) {
		var vurl = true;
		if (path != '' && path != undefined) {
			vurl = validUrl(path);
		}
		if (jQuery.type(name) == "string" && vurl) {
			document.cookie = name + "=" + escape(value) +
				((expires) ? "; expires=" + expires.toGMTString() : "") +
				((path) ? "; path=" + path : "") +
				((domain) ? "; domain=" + domain : "") +
				((secure) ? "; secure" : "");
		}
	}
	
	function _getCookieVal(offset) {
		var endstr = document.cookie.indexOf(";", offset);
		if (endstr == -1) {
			endstr = document.cookie.length;
		}
		return unescape(document.cookie.substring(offset, endstr));
	}

	jQuery('li.text-sizing a:nth-child(1)').click(function(e) {
        e.stopPropagation();
        e.preventDefault();
        _set_font_size('increase');
    });

    jQuery('li.text-sizing a:nth-child(2)').click(function(e) {
        e.stopPropagation();
		e.preventDefault();
        _set_font_size();
    });

    jQuery('li.text-sizing a:nth-child(3)').click(function(e) {
        e.stopPropagation();
        e.preventDefault();
        _set_font_size('decrease');
	});
	
	//fontSize increase & decrease end

	//skiptomain content start
	jQuery('.skip-content > a').bind('click',function(event){
		var $anchor = jQuery(this);
		jQuery('html, body').stop().animate({
			scrollTop: jQuery($anchor.attr('href')).offset().top
			}, 800);
		event.preventDefault();
	});
	//skiptomain content end

	// Sticky Header
	var headerH = jQuery('.header-sticky').outerHeight();
				
	jQuery(".header-sticky").sticky({
		topSpacing:0,
		zIndex:25
	});
	
	jQuery('.header-sticky').on('sticky-end', function() { 
		jQuery('.sticky-wrapper').height(headerH);
	});

	if ( jQuery(window).width() <= 767 ) {
		jQuery(".header-sticky").unstick();
	}

	jQuery('.open-table').click(function() {
		jQuery('.data-table').slideToggle();
		return false;
	});

	jQuery('.trigger-state').click(function() {
		jQuery('.data-table').show();
		return false;
	});

	jQuery('.trigger-state').bind('click',function(event){
		event.preventDefault();
		var $anchor = jQuery(this);
		jQuery('html, body').stop().animate({
			scrollTop: jQuery($anchor.attr('href')).offset().top - headerH
			}, 800);
	});

	jQuery('.trigger-update').bind('click',function(event){
		event.preventDefault();
		var $anchor = jQuery(this);
		jQuery('html, body').stop().animate({
			scrollTop: jQuery($anchor.attr('href')).offset().top - headerH
			}, 800);
		
	});

	jQuery('.trigger-advisories').bind('click',function(event){
		event.preventDefault();
		var $anchor = jQuery(this);
		jQuery('html, body').stop().animate({
			scrollTop: jQuery($anchor.attr('href')).offset().top - headerH
			}, 800);
	});

	jQuery('.trigger-advisories + ul > li').bind('click',function(event){
		event.preventDefault();
		var $anchor = jQuery('.trigger-advisories');
		var $tabID = '#' + jQuery(this).find('a').attr('data-id');
		if(typeof $tabID != typeof undefined){
			jQuery('.tabs-menu li'+ $tabID).trigger('click');
		}
		jQuery('html, body').stop().animate({
			scrollTop: jQuery($anchor.attr('href')).offset().top - headerH
			}, 800);
		
	});

	jQuery('.trigger-awareness').bind('click',function(event){
		event.preventDefault();
		var $anchor = jQuery(this);
		jQuery('html, body').stop().animate({
			scrollTop: jQuery($anchor.attr('href')).offset().top - headerH
			}, 800);
	});

	jQuery('.trigger-faq').bind('click',function(event){
		event.preventDefault();
		var $anchor = jQuery(this);
		jQuery('html, body').stop().animate({
			scrollTop: jQuery($anchor.attr('href')).offset().top - headerH
			}, 800);
	});

	// Go to Top
	jQuery("a[href='#top']").click(function() {
		jQuery("html, body").animate({ scrollTop: 0 }, 1000);
		return false;
	});

	// Canvas Menu
	jQuery('.menuToggle').on('click',function(e) {
		jQuery('.canvas-menu').addClass('active');
		jQuery('.main-body-content').addClass('active');
		return false;
	});
	
	jQuery('.m-close').on('click',function(e) {
		jQuery('.canvas-menu').removeClass('active');
		jQuery('.main-body-content').removeClass('active');
		return false;
	});

	jQuery('body').click(function(e) {
		jQuery('.accessibility-menu li').removeClass("mFocus")
	});

	//keyboard accessing functions start
	function addFocusClass() {

		jQuery('.accessibility-menu li').each(function(index, element) {
			jQuery(this).find('>a').focus(function(e) {
				jQuery(this).parent('li').addClass('mFocus').siblings().removeClass('mFocus');
			});	
		});
		jQuery(".accessibility-menu li.site-lang ul.dropdown-lang li:last-child a").focusout(function(e) {
			jQuery(this).parents('.site-lang').removeClass("mFocus")
		});

		document.addEventListener('keydown', function(e) {
			if (e.keyCode === 9) {
			jQuery('body').addClass('show-focus-outlines');
			}
		});
	
		document.addEventListener('mousedown', function(e) {
			jQuery('body').removeClass('show-focus-outlines');
		});
	
	}

	addFocusClass();
	//keyboard accessing functions end

	// Tabs
	jQuery('.tabs-menu li').click(function(){
		var index = $(this).index();
		jQuery('.tabs-menu li').removeClass('active');
		jQuery(this).addClass('active');
		jQuery('.panes').hide();
		jQuery('.panes').eq(index).show();
		return false;
	});

	// Isotope
	var $container = jQuery('.isotope');
		$container.isotope({
		itemSelector: '.element-item',
		percentPosition: true,
		 masonry: {
			columnWidth: '.element-item'
		}
	});
	
	jQuery('.category-nav ul li a').on( 'click', function() {
			var filterValue = jQuery( this ).attr('data-filter');
			$container.isotope({ filter: filterValue });
			
			jQuery('.category-nav ul li').removeClass('active');
			jQuery(this).parent().addClass('active');
			 return false;
			
		  });
		  
	jQuery('.category-nav ul li:first-child a').trigger('click');


});

jQuery(window).scroll(function() {

	/*var scroll = $(window).scrollTop();    
    if (scroll >= 0) {
  		jQuery(".header-sticky").unstick();
    }*/

	// Scroll to show arrow
	if (jQuery(this).scrollTop()>0)
	 {
		jQuery('a.top').fadeIn();
	 }
	else
	 {
	  jQuery('a.top').fadeOut();
	 }
 });