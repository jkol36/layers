$('#select').selectize({
    create: true,
    optgroupOrder: ["Weddings", "Other Events"]
});


// Animation in hero image using textillate.js
$(function() {
    $('#product').textillate({
	selector: '.texts',
	loop: true,
	minDisplayTime: 7000,
	in: {
	    effect: 'fadeInDown',
	    sync: true
	},
	out: {
	    effect: 'fadeOutDown',
	    sync: true
	}
    });
});

$(function() {
    $('#occasion').textillate({
	selector: '.texts',
	loop: true,
	minDisplayTime: 7000,
	in: {
	    effect: 'fadeInDown',
	    sync: true
	},
	out: {
	    effect: 'fadeOutDown',
	    sync: true
	}
    });
});


// Change the background image when the text animation out begins
currentBg = 0;
$('#occasion').on('outAnimationBegin.tlt', function() {
    var classes = ['hero-caketopper', 'hero-centerpiece', 'hero-cufflinks',
		   'hero-tiebar'];
    
    $('.hero').removeClass(classes[currentBg]);    
    currentBg = currentBg === 3 ? 0 : currentBg + 1;
    $('.hero').addClass(classes[currentBg]);
});


// Width of inspiration pictures should be relative to height for responsiveness
var currentWidth = $('.inspiration').width();
$('.inspiration').css({'height': currentWidth+'px'});


// Datepicker
rome(duedate, {time: false});

