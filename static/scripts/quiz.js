
$(document).ready(function(){
 
    var colsel=["#8d8d8d","#727272","#555555","#adadad"];
    var qds=[["a01", "Demo Ques?", "Option1", "Option2", "Option3", "Option4", "Option5", "Option6", "Option7"], ["a02", "Demo question ?", "Option1", "Option2", "Option3", "Option4", "Option5", "Option6"]];
    var qdm=[["a01", "Demo Ques?", "Option1", "Option2", "Option3", "Option4", "Option5", "Option6", "Option7"], ["a02", "Demo question ?", "Option1", "Option2", "Option3", "Option4", "Option5", "Option6"]];
  
    
    var tq=qds.length+qdm.length;
    var qa=0;
     var qust="Question Unattempted: "+(tq);

      
        $(".score_board>div:nth-child(3)").text(qust);
    for(var i=0;i<qds.length;i++){
        var nq=" <div id="+qds[i][0]+"><div><span>Q"+(i+1)+":</span> "+qds[i][1]+"</div>";
        for(var j=2;j<=11;j++){
            if(qds[i][j]!=null)nq+="<div>"+qds[i][j]+"</div>";
            else break;
        }
        nq+="</div>";
        $(".sc").append(nq);
    }
    for(var i=0;i<qdm.length;i++){
        var nq=" <div id="+qdm[i][0]+"><div><span>Q"+(i+1)+":</span> "+qdm[i][1]+"</div>";
        for(var j=2;j<=11;j++){
            if(qdm[i][j]!=null)nq+="<div>"+qdm[i][j]+"</div>";
            else break;
        }
        nq+="</div>";
        $(".mc").append(nq);
    }
    $(".sc>div>div").click(function(){
        
     
      var sel=-1;
        var curr=-1;
        for(var i=0;i<=10;i++){
          if($(this).parent().children().eq(i).hasClass("selop")){
              sel=i;
             
          }
            if($(this)[0]==$(this).parent().children().eq(i)[0]){
                curr=i;
            }
        }
        if(curr!=0){
            if(sel==-1){
         
$(this).addClass("selop");
         $(this).css("background","white");
                qa++;
                sel=curr;
        }else if(sel==curr){
             $(this).removeClass("selop");
            $(this).css("background",colsel[curr%4]);
            qa--;
            sel=-1;
        }else{
             $(this).addClass("selop");
         $(this).css("background","white");
            $(this).parent().children().eq(sel).removeClass("selop");
            $(this).parent().children().eq(sel).css("background",colsel[sel%4]);
            sel=curr;
        }
        
        
        var ans="";
         for(var i=0;i<=10;i++){
             if(i==sel)ans+="1";
             else ans+="0";
         }
            $.ajax({url: "",dataType:"json",data:{qid:$(this).parent().attr("id"),ans:ans}, success: function(json){
               
        
     }});
           var qast="Question Attempted: "+qa;
           var qust="Question Unattempted: "+(tq-qa);

         $(".score_board>div:nth-child(2)").text(qast);
        $(".score_board>div:nth-child(3)").text(qust);
        var pbp=(qa/tq*100)+"%";
        $(".score_board_progress>div").animate({width:pbp});
        }
    }); 
      $(".mc>div>div").click(function(){
        
     
      var sel=[];
         var ssum=0;
        var curr=-1;
        for(var i=0;i<=10;i++){
          if($(this).parent().children().eq(i).hasClass("selop")){
              sel[i]=1;
              ssum++;
          }else{
              sel[i]=0;
          }
            if($(this)[0]==$(this).parent().children().eq(i)[0]){
                curr=i;
            }
        }
          if(ssum==0){qa++;}
          else if((ssum==1)&&(sel[curr]==1)){qa--;}
          
        if(curr!=0){
            if(sel[curr]==1){
           $(this).removeClass("selop");
            $(this).css("background",colsel[curr%4]);
                
             sel[curr]=0;
        }else{
            $(this).addClass("selop");
         $(this).css("background","white");
           
           sel[curr]=1;
        }
        
       
           var ans="";
         for(var i=0;i<=10;i++){
             if(sel[i]==1)ans+="1";
             else ans+="0";
         }
            $.ajax({url: "",dataType:"json",data:{qid:$(this).parent().attr("id"),ans:ans}, success: function(json){
               
        
     }});
            var qast="Question Attempted: "+qa;
           var qust="Question Unattempted: "+(tq-qa);

         $(".score_board>div:nth-child(2)").text(qast);
        $(".score_board>div:nth-child(3)").text(qust);
        var pbp=(qa/tq*100)+"%";
        $(".score_board_progress>div").animate({width:pbp});
        }
    }); 
     
      var sec=90;
   setInterval(function(){ 
       
      var s=sec--;
       if(s>60){
    var secu=s%60;
    var min=(Math.floor(s/60))%60;
    var hr=Math.floor(s/3600);
    var tr="Time Remaining: ";
    if(hr<10)tr+="0"+hr+":";
    else tr+=hr+":";
     if(min<10)tr+="0"+min+":";
    else tr+=min+":";
     if(secu<10)tr+="0"+secu;
    else tr+=secu;
   $(".score_board>div:nth-child(1)").text(tr); 
       }
       else{
           var tr="Only "+s+"sec left";
           $(".score_board>div:nth-child(1)").text(tr);
       }
      if(s==60) $(".score_board>div:nth-child(1)").css({"background":"red","padding-left":"10px","margin-right":"2%","width":"31%"});
   
   }, 1000);
    

    
});

