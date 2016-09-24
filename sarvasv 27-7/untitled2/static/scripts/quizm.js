$(document).ready(function(){
    
    
    $(".quizmf>form>select").change(function(){
    
      var i;
        for( i=1;i<=parseInt($(".quizmf>form>select").val());i++){
           $(".options>input[name='c"+i+"']").css("display","inline");
            $(".options>input[name='o"+i+"']").css("display","inline");
            
        }
           for(;i<=20;i++) {
              $(".options>input[name='c"+i+"']").css("display","none");
            $(".options>input[name='o"+i+"']").css("display","none"); 
           } 
    });
 
  $(".cross").click(function(){
     $(".quizmf").slideUp();
 }); 
    


   
      $(".quizml>span>select").change(function(){
          alert("nfxgjvjk");
          var jid=$(this).attr("id");
         if($(this).val()=="Edit"){
             alert("nfxgjvjk");
              $.ajax({url: 'http://127.0.0.1:8000/polls/register/test2/',
                  dataType:"json",
                  type:'POST',
                  data:{qid:jid,
                      csrfmiddlewaretoken: ""}, success: function(json){
                $(".quizmf textarea").val("Question here");
                  $(".quizmf input[name='qid']").val("Qid here");
                  var n=parseInt("6");
                    $(".quizmf input[name='nq']").val(""+n);
                   var i;
        for( i=1;i<=n;i++){
           $(".options>input[name='c"+i+"']").css("display","inline");
            $(".options>input[name='o"+i+"']").css("display","inline");
            
        }
           for(;i<=20;i++) {
              $(".options>input[name='c"+i+"']").css("display","none");
            $(".options>input[name='o"+i+"']").css("display","none"); 
           } 
                  
                    $(".quizmf input[name='c1']").val("");
                  $(".quizmf input[name='o1']").val("");
                    $(".quizmf").slideDown();
        
        
     }});
         }              else{
                  
                  $.ajax({url: "http://127.0.0.1:8000/polls/register/test2/",dataType:"json",type :'POST',data:{qid:jid,csrfmiddlewaretoken: '{{ csrftoken }}'}, success: function(json){
                      alert("deleted");
                  }}); 
              }
      });
});
