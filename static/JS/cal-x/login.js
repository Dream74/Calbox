$(function(){
  var recordCursorline ;
  

  function getmycode() {
    var codedone ;
    $.post( '/cal-x/mycode/', { lang: $('#lang').val(), question: $('#question').val(), csrfmiddlewaretoken : $('input[name="csrfmiddlewaretoken"]').val()  },
      function( data ) {
          editor.setOption("onChange", null) ;
          $("#state").text("程式碼下載中");
          editor.setValue( data.code );
          editor.refresh();
          if ( data.readline == "true") 
          {
            codedone = true ;
            editor.setOption("readOnly", true ) ;
            alert( "恭喜你完成此題目!!" ) ;
          }
          else 
          {
            codedone = false ;
            editor.setOption("readOnly", false ) ;
          }
          /*var readline = data.readline.split(",");
          for ( var i = 0; i < readline.length && readline[i] != ""; i++)
          {
            //$("#state").text($("#state").text()+","+readline[i]);
            line = parseInt(readline[i],10)
            editor.setLineClass(line, "activeline");
            editor.setMarker(line,"");
          }*/
    }, 'json')
            .error(function()
            {
              $("#state").text("程式碼下載失敗");
            })
            .complete( function()
            {
              $("#state").text("程式碼下載完成");
              if ( !codedone )
              {
                editor.setOption("onChange", function(){ $("#state").text("程式碼修改中"); scheduleNotification();});
              }
            });
  }

  getmycode();

  $("#lang").change(function(){ //事件發生
    getmycode();
  });

  $("#question").change(function(){ //事件發生
    $("#tabs-2").load("/cal-x/doc/"+ $(this).val());
    getmycode();
  });

  function scheduleNotification() {
    var timeValue = "1";
    var triggerTime = Date.parse(timeValue);
    if (!triggerTime)
    {
      status("Sorry, I didn't understand when you want the notification. Enter &quot;2 minutes&quot; for example.");
      return;
    }
    var remaining = triggerTime.getTime() - (new Date()).getTime();
    if (remaining < 2000) remaining = 2000;
      clearTimeout(timer);
      timer = setTimeout(function()
      {
        var code = editor.getValue();
        if ( code != "" )
        {
          $("#state").text("程式碼上傳中");
          var $form = $( "#codeform" ),
            lang = $form.find( '#lang' ).val(),
            question = $form.find( '#question' ).val(),
            csrf = $form.find( 'input[name="csrfmiddlewaretoken"]' ).val(),
            url = "/cal-x/update_code/" ;
            // alert("action :" + url + "lang :"+ lang+ "question :"+question+"code :" + code + "csrf :" + csrf);
            /* Send the data using post and put the results in a div */
            $.post( url, { lang: lang, question: question, code : code, csrfmiddlewaretoken : csrf  },
              function( data ) {
                //var content = $( data ).find( '#content' );
                editor.refresh();
              }, 'text')
                  .error(function()
                   {
                     $("#state").text("程式碼上載失敗");
                   })
                  .complete( function()
                       {
                          $("#state").text("程式碼上傳成功" );
                       });
        }
      }, remaining);
    }
});
var timer ;
