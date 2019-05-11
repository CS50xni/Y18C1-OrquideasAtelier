$(document).foundation()

$(function() {
    $(window).scroll(function() {
      var winTop = $(window).scrollTop();
      if (winTop >= 25) {
        $("body").addClass("sticky-shrinknav-wrapper");
      } else{
        $("body").removeClass("sticky-shrinknav-wrapper");
      }
    });
  });