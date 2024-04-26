$(document).ready(function() {
  $( "button" ).click(function() {
    var texto1 = $('#nombreCarrera').text();
    var texto2 = $('#nombreUniversidad').text();
    $('#mensajeFinal').text("Su carrera es: "+ texto1 + ". Su universidad es: "
      + texto2);

    $('#mensajeFinal').css( "color", "red" );
    console.log(texto1);
  });

  $("h1").on( "mouseover", function() {
      $('#nombreUniversidad').css( "color", "blue" );
  });

  $("#nombreCarrera").on( "mouseover", function() {
      $('#nombreUniversidad').css( "color", "green" );
  });

  $("#nombreUniversidad").on( "mouseover", function() {
      $('#nombreUniversidad').css( "color", "black" );
      $('body').css( "background", "black" );
  });


});
