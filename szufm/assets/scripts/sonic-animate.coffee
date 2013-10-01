$ ->

  LINE_HEIGHT = 52;
  DEFAULT_MIN_HEIGHT = 1;
  DEFAULT_MAX_HEIGHT = LINE_HEIGHT;

  set_height = (obj, min, max) ->
    max = DEFAULT_MAX_HEIGHT if typeof(max) == 'undefined' or parseInt(max) > DEFAULT_MAX_HEIGHT;
    min = DEFAULT_MIN_HEIGHT if typeof(min) == 'undefined' or parseInt(max) < DEFAULT_MIN_HEIGHT;
    random_height = parseInt(Math.random()*(max - min) + min);
    obj.css({'height': random_height + 'px', 'margin-top': (LINE_HEIGHT - random_height) / 2});

  $('span.sonic').append("<div class='sonic-animate-container'></div>");
  for i in [0..119]
    $('.sonic-animate-container').append("<span index='" + i + "' class='sonic-animate-line'></span>")

  sonic_beat = () ->
    @sonic_beat_id = setInterval(->
      $('.sonic-left .sonic-animate-line').each ->
        index = parseInt $(this).attr('index')
        max_height = index / 4;
        set_height $(this), DEFAULT_MIN_HEIGHT, max_height;
      $('.sonic-right .sonic-animate-line').each ->
        index = parseInt $(this).attr('index')
        max_height = (120 - index) / 4;
        set_height $(this), DEFAULT_MIN_HEIGHT, max_height;
    , 150);
    @sonic_beat_id

  $('.start-button').mouseover ->
    $('.sonic').removeClass('sonic-hide').addClass('sonic-show');
    sonic_beat_id = sonic_beat()
  $('.start-button').mouseout ->
    $('.sonic').removeClass('sonic-show').addClass('sonic-hide');
    window.clearInterval sonic_beat_id
