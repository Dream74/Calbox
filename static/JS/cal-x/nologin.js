$(function(){
  $("#question").change(function(){ //事件發生
    $("#tabs-2").load("/cal-x/doc/"+ $(this).val());
  });
});
