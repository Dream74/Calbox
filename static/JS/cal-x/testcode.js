$(function() {
  /* attach a submit handler to the form */
  $("#codeform").submit(function(event) {
    /* stop form from submitting normally */
    event.preventDefault();
    // $form.find( 'value="挑戰"' ).addClass( "background: green;" ) ;
    $("#state").text("程式執行中");
    /* get some values from elements on the page: */
    var $form = $( this ),
        lang = $form.find( '#lang' ).val(),
        Cin = $form.find( '#input_textarea' ).val(),
        csrf = $form.find( 'input[name="csrfmiddlewaretoken"]' ).val(),
        code = editor.getValue(),
        url = $form.attr( 'action' );
        $form.find('input[type="submit"]').attr("disabled", true);
    /* Send the data using post and put the results in a div */
     $.post( url, { lang: lang, code : code, csrfmiddlewaretoken : csrf, Cin : Cin  },
      function( data ) {
        $("#output_textarea").val(data.output);
        $("#message").val(data.compiler_warn);
      }, 'json' )
                .error(function()
                {  
                  $("#message").val(""); 
                  alert( "你的程式執行過程中，發生錯誤!"  ) ;
                })
                .complete( function() 
                {
                  $form.find('input[type="submit"]').attr("disabled", false);
                });
  });
});
