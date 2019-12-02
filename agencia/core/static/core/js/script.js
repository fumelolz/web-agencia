$(document).ready(function() {
	$('.menu-toggle').on('click',function(){
		$('.nav').toggleClass('showing');
		$('.nav ul').toggleClass('showing');
	});


$('.package-wrapper').slick({
  nextArrow: $('.nexti'),
  prevArrow: $('.previ'),
  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 3000
});

$('.testimonial-wrapper').slick({
  nextArrow: $('.nexte'),
  prevArrow: $('.preve'),
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 3000
});

	$('.post-wrapper').slick({
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 3000,
		nextArrow: $('.next'),
		prevArrow: $('.prev'),
		responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ],
	});
});	

jQuery.datetimepicker.setLocale('es');
jQuery('#id_date_posted').datetimepicker({
  timepicker:false,
  maxDate:0,
  format:'Y-m-d h:i',
});