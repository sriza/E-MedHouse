(function ($) {
  'use strict';

  // Preloader
  $(window).on('load', function () {
    $('#preloader').fadeOut('slow', function () {
      $(this).remove();
    });
  });

  
  // Instagram Feed
  if (($('#instafeed').length) !== 0) {
    var accessToken = $('#instafeed').attr('data-accessToken');
    var userFeed = new Instafeed({
      get: 'user',
      resolution: 'low_resolution',
      accessToken: accessToken,
      template: '<a href="{{link}}"><img src="{{image}}" alt="instagram-image"></a>'
    });
    userFeed.run();
  }

  // setTimeout(function () {
  //   $('.instagram-slider').slick({
  //     dots: false,
  //     speed: 300,
  //     // autoplay: true,
  //     arrows: false,
  //     slidesToShow: 6,
  //     slidesToScroll: 1,
  //     responsive: [{
  //         breakpoint: 1024,
  //         settings: {
  //           slidesToShow: 4
  //         }
  //       },
  //       {
  //         breakpoint: 600,
  //         settings: {
  //           slidesToShow: 3
  //         }
  //       },
  //       {
  //         breakpoint: 480,
  //         settings: {
  //           slidesToShow: 2
  //         }
  //       }
  //     ]
  //   });
  // }, 1500);


  // e-commerce touchspin
  // $('input[name=\'product-quantity\']').TouchSpin();


  // Video Lightbox
  $(document).on('click', '[data-toggle="lightbox"]', function (event) {
    event.preventDefault();
    $(this).ekkoLightbox();
  });


  // Count Down JS
  // $('#simple-timer').syotimer({
  //   year: 2022,
  //   month: 5,
  //   day: 9,
  //   hour: 20,
  //   minute: 30
  // });

  // Hero Slider
  $('.hero-slider').slick({
    autoplay: true,
    infinite: true,
    arrows: true,
    prevArrow: '<button type=\'button\' class=\'heroSliderArrow prevArrow tf-ion-chevron-left\' aria-label=\'button to click Previous slide\'></button>',
    nextArrow: '<button type=\'button\' class=\'heroSliderArrow nextArrow tf-ion-chevron-right\' aria-label=\'button to click Next slide\'></button>',
    dots: true,
    autoplaySpeed: 7000,
    pauseOnFocus: false,
    pauseOnHover: false
  });
  $('.hero-slider').slickAnimation();


})(jQuery);

  // e-commerce touchspin
  $('input[name=\'product-quantity\']').TouchSpin();


$(document).ready(function(){
  //datepicker
  $('.datepicker').datepicker({format: "MM/dd/yyyy hh:mm:ss"});
  

  //datetimepicker
  $('.form_datetime').datetimepicker({
    //language:  'fr',
    weekStart: 1,
    todayBtn:  1,
    autoclose: 1,
    todayHighlight: 1,
    startView: 2,
    forceParse: 0,
    showMeridian: 1
  });

//prescription doctor
	$('#MybtnModal').click(function(){
		$('#Mymodal').modal('show')
	});
});

//upload file
// $('#OpenfileUpload').click(function(){ $('#fileupload').trigger('click'); });

$(function () {
  $(".datetimepicker").datetimepicker(
    {
      format: 'Y-m-d H:i',
    }
  );
});

//for model-box for only one model
// $(document).ready(function(){
//   $("#my-circle-btn").click(function() {
//       $(".modal-backdrop").css("display", "none");
//   });
// });

// $(function () {
//   $("#datetimepicker").datetimepicker();
// });

$(document).ready(function() {

  $('#btn-reset').on('click', function(){
    console.log('hello');
    window.localStorage.setItem('text-size', 0);
    window.localStorage.setItem('high-light', 0);
    window.localStorage.setItem('contrast', 0);
    window.localStorage.setItem('text-height', 0);
    window.localStorage.setItem('text-space', 0);
    window.localStorage.setItem('font-family', 0);
    window.localStorage.setItem('cursor', 0);

    location.reload();
});

  //contrast
  $('#contrast').on('click', function() {
    var contrastCount = $(this).attr('contrast-count');
  
      // $('*').each(function() {
  
      //   if(contrastCount == 2){
         
      //     $(this).css("filter", "invert(0)");
      //     $('section').removeClass('invert-yellow');
      //     $('.section-odd, .products').removeClass('invert');
      //     $('.section-even, .navbar, .navbar a').removeClass('invert-black');
      //     $('button').removeClass('button-invert');

      //   }else if(contrastCount == 1){
      //     $('img, .slider-item').css("filter", "invert(0.8)");
      //     $('section').addClass('invert-yellow');
      //     $('.section-odd, .products').addClass('invert');
      //     $('.section-even, .navbar, .navbar a').addClass('invert-black');
      //     $('button').addClass('button-invert');
      //     $(this).css("filter", "saturate(1)");

      //   }else{
      //     $('img, i, .text-info, .slider-item').css("filter", "saturate(0)");

      //   }
  
      // });
  
      if(contrastCount == 2){
        $(this).attr('contrast-count', 0);
        window.localStorage.setItem('contrast', 0);
        $("#check-contrast, #contrast1, #contrast2").css("visibility", "hidden");
      }else if(contrastCount == 0){
        $(this).attr('contrast-count', parseInt(contrastCount) + 1);
        window.localStorage.setItem('contrast', parseInt(contrastCount) + 1);
        $("#check-contrast, #contrast1").css("visibility", "visible");

      }else{
        $(this).attr('contrast-count', parseInt(contrastCount) + 1);
        window.localStorage.setItem('contrast', parseInt(contrastCount) + 1);
        $("#check-contrast, #contrast2").css("visibility", "visible");
      }
      location.reload();
      checkAccessible();
  });
  
  //text-size
  $('#text-size').on('click', function() {
    var text = $(this).attr('text-size');

      $(':not(.noBig)').each(function() {
          var fontsize = parseInt($(this).css('font-size'));

          if(text == 2){
            newFontsize = (fontsize - 10) + 'px';
            $(this).css('font-size', newFontsize);
          }else{
            newFontsize = (fontsize + 5) + 'px';
            $(this).css('font-size', newFontsize);  
          }

      });

      if(text == 2){
        $(this).attr('text-size', 0);
        window.localStorage.setItem('text-size', 0);
        $("#big1, #big2, #check-big").css("visibility","hidden");
      }else{
        $(this).attr('text-size', parseInt(text) + 1);
        window.localStorage.setItem('text-size', parseInt(text) + 1);
        $("#check-big").css("visibility","visible");

        if(text == 0){
          $("#big1").css("visibility","visible");
        }
        else if(text == 1){
          $("#big2").css("visibility","visible");
        }

      }

      checkAccessible();
  });
  
 //font-family
 $('#fonts').on('click', function() {
  var font_count = $(this).attr('font-family');


    $('*').each(function() {
        if(font_count == 1){
          $('h1,h2,h3,li,a,p,span,button').removeClass('dyslexia');
        }else{
          $('h1,h2,h3,li,a,p,span,button').addClass('dyslexia');
        }

    });

    if(font_count == 1){
      $('#fonts').attr('font-family', 0);
      window.localStorage.setItem('font-family', 0);
      $("#check-font").css("visibility","hidden");
    }else{
      $('#fonts').attr('font-family', parseInt(font_count) + 1);
      window.localStorage.setItem('font-family', parseInt(font_count) + 1);
      $("#check-font").css("visibility","visible");
    }

    checkAccessible();
});

//curser
$('#cursor').on('click', function() {
  var count = $(this).attr('cursor-count');
 
    if(count == 1){
      $('#cursor').attr('cursor-count', 0);
      window.localStorage.setItem('cursor', 0);
      $("#check-cursor").css("visibility","hidden");
    }else{
      $('#cursor').attr('cursor-count', parseInt(count) + 1);
      window.localStorage.setItem('cursor', parseInt(count) + 1);
      $("#check-cursor").css("visibility","visible");
    }
    location.reload();
    checkAccessible();
});
  
// text-spacing
  $('#text-spacing').on('click', function() {
    var text_space = $(this).attr('text-space');
    
      $(':not(.noBig)').each(function() {
          var fontSpace = parseInt($(this).css('letter-spacing'));
      
          if(text_space  == 2){
            newfontSpace = 0 + 'px';
            $(this).css('letter-spacing', newfontSpace);
          }else{
            newfontSpace = (fontSpace + 2) + 'px';
            $(this).css('letter-spacing', newfontSpace);
          }

      });
      
      if(text_space == 2){
        $(this).attr('text-space', 0);
        window.localStorage.setItem('text-space', 0);
        $("#one, #two, #check-space").css("visibility","hidden");
      }else{
        $(this).attr('text-space', parseInt(text_space) + 1);
        $("#check-space").css("visibility","visible");
        window.localStorage.setItem('text-space', parseInt(text_space) + 1);

        if(text_space == 0){
          $("#one").css("visibility","visible");
        }
        else if(text_space == 1){
          $("#two").css("visibility","visible");
        }

      }

      checkAccessible();
  });

   
// line-height
$('#lineHeight').on('click', function() {
  var text_height = parseInt($(this).attr('text-height'));
  console.log(text_height);
  var height = parseInt($(this).css('line-height'));

    $(':not(.noBig, .noHeight)').each(function() {
        var lineHeight = parseInt($(this).css('line-height'));
    
        if(text_height  == 2){
          newlineHeight = height + 'px';
          $(this).css('line-height', newlineHeight);
        }else{
          newlineHeight = (lineHeight + 6) + 'px';
          $(this).css('line-height', newlineHeight);
        }

    });

    if(text_height == 2){
      $(this).attr('text-height', 0);
      window.localStorage.setItem('text-height', 0);
      $("#height1, #height2, #check-height").css("visibility","hidden");
     
    }else{
      $(this).attr('text-height', parseInt(text_height) + 1);
      window.localStorage.setItem('text-height', parseInt(text_height) + 1);
      $("#check-height").css("visibility","visible");

      if(text_height == 0){
        $("#height1").css("visibility","visible");
      }
      else if(text_height == 1){
        $("#height2").css("visibility","visible");
      }
    }

    checkAccessible();
  

});

   
// highlightlink
$('#highlight').on('click', function() {
  var highlight = $(this).attr('text-highlight');

    $(':not(.noBig)').each(function() {

      if(highlight == 1){
       
        $('a').removeClass('highlight');
      }else{
        $('a:not(.noBig)').addClass('highlight');
      }

    });

    if(highlight == 1){
      $(this).attr('text-highlight', 0);
      window.localStorage.setItem('high-light', 0);
      $("#check-highlight").css("visibility", "hidden");
   
    }else{
      $(this).attr('text-highlight', parseInt(highlight) + 1);

      window.localStorage.setItem('high-light', parseInt(highlight) + 1);
      $("#check-highlight").css("visibility", "visible");
    }

    checkAccessible();
});

function checkAccessible(){

  if((parseInt(window.localStorage.getItem('high-light'))+parseInt(window.localStorage.getItem('text-height'))+parseInt(window.localStorage.getItem('text-size'))+parseInt(window.localStorage.getItem('text-space'))+parseInt(window.localStorage.getItem('contrast')))>0){
    $("#check-ace").css("visibility","visible");
  } else {
    $("#check-ace").css("visibility","hidden");
  }

}

});

$(document).ready(function(){
  
  // contrast

    var contrastCount = window.localStorage.getItem('contrast');

    if(!Number.isNaN(parseInt(contrastCount))){
      $('#contrast').attr('contrast-count', contrastCount);
     
      if(contrastCount == 1){
        $('img, i, .text-info, .slider-item').css("filter", "saturate(0)");
        $("#check-contrast, #contrast1").css("visibility", "visible");


      } else if(contrastCount == 2){
        $('img, .slider-item').css("filter", "invert(0.8)");
        $('section').addClass('invert-yellow');
        $('.section-odd,.products').addClass('invert');
        $('.section-even, .navbar, .navbar a').addClass('invert-black');
        $('button').addClass('button-invert');
        $("#check-contrast, #contrast1, #contrast2").css("visibility", "visible");
      }else{
        $('img, .slider-item').css("filter", "invert(0)");
        $('section').removeClass('invert-yellow');
        $('.section-odd,.products').removeClass('invert');
        $('button').removeClass('button-invert');
        $('.section-even, .navbar, .navbar a').removeClass('invert-black');
        $("#check-contrast, #contrast1, #contrast2").css("visibility", "hidden");
      }
    }else{
      window.localStorage.setItem('contrast', 0);
    }
    
  //text-size
        var text_size = window.localStorage.getItem('text-size');
        if(!Number.isNaN(parseInt(text_size))){
            $(':not(.noBig)').each(function() {
              var fontsize = parseInt($(this).css('font-size'));

              newFontsize = (fontsize + (parseInt(text_size) * 5)) + 'px';
              $(this).css('font-size', newFontsize);

            });

            $('#text-size').attr('text-size', text_size);


            if(text_size == 1){
              $("#big1, #check-big").css("visibility","visible");
            }
            else if(text_size == 2){
             $("#big2, #big1, #check-big").css("visibility","visible");
            }
        }else{
          window.localStorage.setItem('text-size', 0);
        }
       
    //font-family
    var font_fam = window.localStorage.getItem('font-family');
    if(!Number.isNaN(parseInt(font_fam))){
      $('#fonts').attr('font-family', font_fam);

      if(font_fam == 0){
        $('h1,h2,h3,li,a,p,span, button').removeClass('dyslexia');
        $("#check-font").css("visibility","hidden");
      }else{
        $('h1,h2,h3,li,a,p,span, button').addClass('dyslexia');
        $("#check-font").css("visibility","visible");
      }
    }else{
      window.localStorage.setItem('font-family', 0);
    }

    //curser
    var cursor = window.localStorage.getItem('cursor');
    if(!Number.isNaN(parseInt(cursor))){
      $('#cursor').attr('cursor-count', cursor);
      if(cursor == 0){
        $("#check-cursor").css("visibility","hidden");
      }else{
        $(document).ready(function(){
        $('*').changeCursor('/static/images/cursor.png',32,0);
        });
        $("#check-cursor").css("visibility","visible");
      }
    }else{
      window.localStorage.setItem('cursor', 0);
    }
    //text-spacing

    var text_space = window.localStorage.getItem('text-space');

    if(!Number.isNaN(parseInt(text_space))){
      $(':not(.noBig)').each(function() {
        var fontSpace = parseInt($(this).css('letter-spacing'));
  
        newFontSpace = (fontSpace + (parseInt(text_space) * 1)) + 'px';
        $(this).css('letter-spacing', newFontSpace);
  
      });
  
      $('#text-spacing').attr('text-space', text_space);
  
  
      if(text_space == 1){
        $("#one, #check-space").css("visibility","visible");
      }
      else if(text_space == 2){
        $("#one, #two, #check-space").css("visibility","visible");
      }
    }else{
      window.localStorage.setItem('text-space', 0);
    }
   
    // highlight link

    var highlight = window.localStorage.getItem('high-light');

    if(!Number.isNaN(parseInt(highlight))){
      $('#highlight').attr('text-high', highlight);
  
      if(highlight == 0){
        $('a:not(.noBig)').removeClass('highlight');
        $("#check-highlight").css("visibility", "hidden");
      }
      else{
        $('a:not(.noBig)').addClass('highlight');
        $("#check-highlight").css("visibility", "visible");
      }
    }else{
      window.localStorage.setItem('high-light', 0);
    }

    // line-height
    
    var text_height = window.localStorage.getItem('text-height');
    if(!Number.isNaN(parseInt(text_height))){
      $(':not(.noBig, .noHeight)').each(function() {
        var lineHeight = parseInt($(this).css('line-height'));
        
        newlineHeight = (lineHeight + (text_height) * 6) + 'px';
        $(this).css('line-height', newlineHeight);  
      });
  
      $('#lineHeight').attr('text-height', text_height);
  

        if(text_height == 1){
          $("#height1,#check-height").css("visibility","visible");
        }
        else if(text_height == 2){
          $("#height2, #height1,#check-height").css("visibility","visible");
        }
      }else{
      window.localStorage.setItem('text-height', 0);

    }

    //check accessible
    if((parseInt(window.localStorage.getItem('high-light'))+parseInt(window.localStorage.getItem('text-height'))+parseInt(window.localStorage.getItem('text-size'))+parseInt(window.localStorage.getItem('font-family'))+parseInt(window.localStorage.getItem('cursor'))+parseInt(window.localStorage.getItem('text-space'))+parseInt(window.localStorage.getItem('contrast')))>0){
      $("#check-ace").css("visibility","visible");
    } else {
      $("#check-ace").css("visibility","hidden");
    }

});



//browser cusor
(function ($) {
  var browser = (function () {

      var ua = navigator.userAgent,
          tem,
          M = ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || [];

      if (/trident/i.test(M[1])) {
          tem = /\brv[ :]+(\d+)/g.exec(ua) || [];
          return 'IE ' + (tem[1] || '');
      }

      if (M[1] === 'Chrome') {
          tem = ua.match(/\bOPR\/(\d+)/);
          if (tem !== null) return 'Opera ' + tem[1];
      }

      M = M[2] ? [M[1], M[2]] : [navigator.appName, navigator.appVersion, '-?'];
      if ((tem = ua.match(/version\/(\d+)/i)) !== null) M.splice(1, 1, tem[1]);
      return M.join(' ');
  })();

  $.fn.changeCursor = function (cursorPicUrl, dx, dy, zIndex) {

      function inFunction(e) {
          $cursor.show();
          return false;
      }

      function outFunction(e) {
          $cursor.hide();
          return false;
      }

      function moveFunction(e) {
          cursor.style.left = e.clientX - dx + 'px';
          cursor.style.top = e.clientY - dy + 'px';
      }

      //defaults
      dx = dx || 0;
      dy = dy || 0;
      zIndex = zIndex || 1000;

      var IE      =   browser.indexOf('IE') != -1;
      var version =   +browser.replace( /^\D+/g, '');
      var $cursor =   $('#custom-cursor');
      var cursor  =   $cursor[0];
      var excluded=   'a, input';

      if ( !( IE && version < 9 ) ) {
          if ( $cursor.length === 0 ) {
$cursor = $('<svg id="custom-cursor"></svg>')// svg - hack for rendering performance
                  .css({
                      background: 'url("' + cursorPicUrl + '") no-repeat left top',
                      position:   'fixed',
                      display:    'block',
                      'z-index':  3,
                      'pointer-events': 'none',
                      transform: 'translateZ(0)'// hack to make this element rendering by GPU
                  })
                  .hide();
              $('body').append( $cursor[0] );
              cursor = $cursor[0];
            

          }
          this.on( "mouseenter", inFunction )
              // .on( "mouseleave", outFunction )
              .on( "mousemove",  moveFunction);
              
              // .css( 'cursor', 'none')
              // .css( 'cursor', 'none');

          $(excluded)
              // .on( "mouseenter", outFunction )
              // .on( "mouseleave", inFunction);
      }

      return this;
  };

})(jQuery);

//cursor
// $(document).ready(function(){
//   $('*').changeCursor('/static/images/cursor.png',32,0);
// });