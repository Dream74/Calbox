$(function() {
  /* attach a submit handler to the form */
  $("#codeform").submit(function(event) {
    /* stop form from submitting normally */
    event.preventDefault();
    if ( $('#question > option[value="'+ $('#question').val() +'"]').attr('title') == '已完成' )
    {
      alert('本題目恭喜已經完成!!');
      return;
    }

    // $form.find( 'value="挑戰"' ).addClass( "background: green;" ) ;
    $("#state").text("程式執行中");
    /* get some values from elements on the page: */
    var $form = $( this ),
        lang = $form.find( '#lang' ).val(),
        question = $form.find( '#question' ).val(),
        csrf = $form.find( 'input[name="csrfmiddlewaretoken"]' ).val(),
        code = editor.getValue(),
        supermode ,
        remestype ,
        url = $form.attr( 'action' );
    if ( $("#supermode").attr('checked') )
    {
       supermode = true ;
       remestype = "text" ;
    }
    else
    {
       supermode = false ; 
       remestype = "json" ;
    }
    $form.find('input[type="submit"]').attr("disabled", true);
    /* Send the data using post and put the results in a div */
     $.post( url, { lang: lang, question: question, code : code, csrfmiddlewaretoken : csrf, supermode : supermode  },
      function( data ) {
          if ( supermode )
            $("#message").val( data );
          else if ( data.type == "Run OK")
          {
            // $("#message").val(data.message);
            alert( "你的程式通過所有測試數據"  ) ;
            $("#message").val("");
            $('#question > option[value="'+ $('#question').val() +'"]').css('color', 'red').attr('title', '已完成') ;
          }
          else if ( data.type == "Styple error")
          {
            $("#message").val(data.message);
          }
          else if ( data.type == "Complit error")
          {
            alert( "你的程式編譯時，發生錯誤"  ) ;
            $("#message").val(data.message);
          }
          else if ( data.type == "Run time error")
          {
            alert( "你的程式執行過程中，發生錯誤"  ) ;
            $("#message").val(data.message);
          }
          else if ( data.type == "Infinite loop")
          {
            alert( "你的程式疑似有無窮迴圈"  ) ;
            $("#message").val('');
          }
          else
          {
            alert( "你無法通過測試數據"  ) ;
            $("#message").val(data.message);
          }
      }, remestype )
                .error(function()
                       {  
                          $("#message").val(""); 
                          alert( "你的程式執行過程中，發生錯誤!"  ) ;
                       })
                .complete( function() 
                           {
                             $("#state").text("程式執行完成");
                             $form.find('input[type="submit"]').attr("disabled", false);
                           });
  });
});
