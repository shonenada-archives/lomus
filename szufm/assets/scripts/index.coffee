$ ->
  # Initial layout
  $("#footer").removeClass("absolute-footer").addClass("relative-footer");
  $(".bracket").css({'opacity': '0'});
  $(".FM").animate({'width': '-420px', 'opacity': '0'}, 1);

$ ->
  # Define animates
  bracket_slide = (timeout, callback) ->
    $(".bracket").animate({"opacity": "1"}, timeout, callback);

  showTitle = (timeout, callback) ->
    $(".bracket").css("margin": "0px");
    $(".FM").animate({'width': '+420px', 'opacity': '1'}, timeout, callback);

  showSubTitle = (timeout, callback) ->
    $('h2.sub-title').animate({'opacity': '1'}, timeout, callback);

  bracket_slide 400, ->
    showTitle 1000, ->
      showSubTitle 500;
