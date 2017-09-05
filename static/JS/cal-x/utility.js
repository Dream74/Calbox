var editor ;
$(function() {
  // jquery-ui
  //$( "input:submit, input:button, button" ).button();
  // $( "select" ).selectmenu({style:'dropdown'});
  // jquery-ui
 
  $( "#tabs" ).tabs({
    ajaxOptions: {
      error: function( xhr, status, index, anchor ) {
        $( anchor.hash ).html(
          "Couldn't load this tab. We'll try to fix this as soon as possible. " +
          "If this wouldn't be a demo." );
      }
    },
    show : function(event, ui) {
      if ( ui.index == 1 )
      {
        $(document).bind('keydown', 'F9', function() {
          $("#run_code_button").click();
        });
        if ( editor )editor.refresh();
      } else 
      {
        $(document).unbind('keydown', false);
      }
    }
  });

  $("#tabs-2").load("/cal-x/doc/" + $("#question").val());
  var savecode ;
  editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    lineWrapping: true,
    lineNumbers: true,
    matchBrackets: true,
    tabSize : 2 ,
    mode: "text/x-csrc",
	onKeyEvent : function ( a1,a2 ) {
		if ( a2.type == "keydown" && ( a2.keyCode == 13 || a2.keyCode == 8 || a2.keyCode == 46 ) )
			$('.CodeMirror-scroll').attr( "style","overflow:"+( (editor.lineCount() >= 33 ) ? "auto" : "hidden" )+";" );
		
		return false;
	},
    extraKeys : {
      "Ctrl-C":function(e) { 
        savecode = editor.getSelection();
        window.clipboardData.setData('Text',"請別嘗試把Code 複製到外面");
        // alert("Hello-C"+savecode) ;
       },
      "Ctrl-V":function(e) { 
        editor.replaceSelection(savecode);
        // alert("Hello-V"+ savecode);
       }
    }
  });


  $("#code_theme").change(function(){ //事件發生
    editor.setOption("theme", $(this).val());
  });

  $("#example").click(function(){ //事件發生
    $.get("/cal-x/example_code/"+ $('#lang').val(),
      function( data ){
        editor.setValue( data );
      });
  });

});
var _wau = _wau || []; _wau.push(["tab", "75jdavtqv63f", "0l6", "right-upper"]);(function() { var s=document.createElement("script"); s.async=true; s.src="http://widgets.amung.us/tab.js";document.getElementsByTagName("head")[0].appendChild(s);})();
