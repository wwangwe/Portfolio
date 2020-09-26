(function ($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 55)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function () {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 65
  });

})(jQuery); // End of use strict

$(function () {
  $(document).scroll(function () {
    var $nav = $(".navbar");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height() + 300);
  });
});

// Dark-Mode

function darkmode(x) {
  //toggle between icons
  document.body.classList.toggle('dark-mode');
  x.classList.toggle('fa-sun');
  x.classList.toggle('fa-spin');

  // navigation bar
  var nav = document.getElementById('mainNav');
  nav.classList.toggle('navbar-dark');
  nav.classList.toggle('bg-dark');

  var navbar = document.getElementById('navbarResponsive');
  navbar.classList.toggle('bg-dark');

  // images
}