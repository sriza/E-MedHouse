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

  //Hero Slider
  // $('.hero-slider').slick({
  //   // autoplay: true,
  //   infinite: true,
  //   arrows: true,
  //   prevArrow: '<button type=\'button\' class=\'heroSliderArrow prevArrow tf-ion-chevron-left\'></button>',
  //   nextArrow: '<button type=\'button\' class=\'heroSliderArrow nextArrow tf-ion-chevron-right\'></button>',
  //   dots: true,
  //   autoplaySpeed: 7000,
  //   pauseOnFocus: false,
  //   pauseOnHover: false
  // });
  // $('.hero-slider').slickAnimation();


})(jQuery);

//picker
$(function(){
  console.log('here');
  $('#datepicker-test').datepicker()
});

//chat bot

const messages = [
  "you are not serious",
  "kikiki so what?",
  "where did you come from",
  "lol are you kidding me",
  "and so  what do u mean"
];
let counter = 0;
const chatContainer = document.querySelector(".container");
const chatArea = document.querySelector(".message-body");
const text = document.querySelector("#text");
const form = document.querySelector(".form");

function isOverflown(element) {
  return (
    element.scrollHeight > element.clientHeight ||
    element.scrollWidth > element.clientWidth
  );
}

function scroll() {
  chatArea.scroll(0,chatArea.scrollHeight);
}

function reply(msg) {
  let li = document.createElement("li");
  li.innerHTML = msg;
  li.classList.add("chatbox");
  li.classList.add("chatbox-incoming");
  chatArea.append(li);
  scroll();
}


//EVENT LISTENERS
text.addEventListener("focus", () => {
  chatContainer.scrollTop = chatArea.scrollHeight + 560;
});



form.addEventListener("submit", e => {
  e.preventDefault();
  msg = text.value;
  let li = document.createElement("li");
  li.innerHTML = msg;
  li.classList.add("chatbox");
  li.classList.add("chatbox-outgoing");
  chatArea.append(li);
  scroll();
  text.value = "";
  // chatContainer.scrollTop =chatContainer.scrollHeight;
  text.focus();
  setTimeout(reply, 1000, messages[counter]);
  counter++;
  if (counter == messages.length) {
    counter = 0;
  }
});


window.onload = ()=>{
  reply("hi please type a message for me")
}




//buble body
const body = document.querySelector('body');





// chatpot
function openChatBubble() {
  var element = document.getElementById("chat-bubble");
  element.classList.toggle("open")
}

form.addEventListener("keyup", function(event) {
if (event.keyCode === 13) {
  msg = text.value;
  let li = document.createElement("li");
  li.innerHTML = msg;
  li.classList.add("chatbox");
  li.classList.add("chatbox-outgoing");
  chatArea.append(li);
  scroll();
  text.value = "";
  // chatContainer.scrollTop =chatContainer.scrollHeight;
  text.focus();
  setTimeout(reply, 1000, messages[counter]);
  counter++;
  if (counter == messages.length) {
    counter = 0;
  }
}
});

//prescription doctor
$(document).ready(function(){
	$('#MybtnModal').click(function(){
		$('#Mymodal').modal('show')
	});
});

//upload file
$('#OpenfileUpload').click(function(){ $('#fileupload').trigger('click'); });


