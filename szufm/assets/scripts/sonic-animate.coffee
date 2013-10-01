$ ->

  LINE_HEIGHT = 52;
  MIN_HEIGHT = 10
  DEFAULT_MAX_LENGTH = LINE_HEIGHT;

  set_height = (obj, max) ->
    max = DEFAULT_MAX_LENGTH if typeof(max) == 'undefined' or parseInt(max) > DEFAULT_MAX_LENGTH;
    random_height = parseInt(Math.random()*(max - MIN_HEIGHT) + MIN_HEIGHT);
    obj.css({'height': random_height + 'px', 'margin-top': (LINE_HEIGHT - random_height) / 2});

  $('span.sonic').append("<div class='sonic-animate-container'></div>");
  for i in [0..119]
    $('.sonic-animate-container').append("<span id='" + i + "' class='sonic-animate-line'></span>")
  $('.sonic-animate-line').each ->
      set_height $(this);
  setInterval(->
    $('.sonic-animate-line').each ->
      set_height $(this);
  , 150);
