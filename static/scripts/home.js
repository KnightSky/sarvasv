
    $(".slider").ready(function(){
        slider();
        $(".a24").click(function(){
            $(".slider>*").css({"opacity":"0"});
            $(".a1").css({"width":"300px","-webkit-animation":"none","animation":"none","top":"-=100px"});
            $(".a2").css({"width":"264px","top":"5px"});
            $(".a3").css({"font-size":"60px","top":"20px","left":"0px"});
            $(".a4").css({"background":"chartreuse"});
            $(".a5").css({"background":"deepskyblue"});
            $(".a6").css({"background":"orange"});
            $(".a7").css({"background":"hotpink"});
            $(".a7").css({"background":"hotpink"});
            $(".a8").css({"top":"-2120px","left":"50px"});
            $(".a9").css({"top":"-2130px","left":"650px"});
            $(".a10").css({"top":"-2290px","left":"190px"});
            $(".a11").css({"top":"-1920px","left":"90px"});
            $(".a12").css({"top":"-2150px","left":"40px"});
            $(".a13").css({"top":"-2250px","left":"40px"});
            $(".a14").css({"top":"-2380px","left":"40px"});
            $(".a15").css({"top":"-2450px","left":"40px"});
            $(".a16").css({"top":"-2560px","left":"50px"});
            $(".a17").css({"top":"-2570px","left":"670px"});
            $(".a18").css({"top":"-2730px","left":"230px"});
            $(".a19").css({"top":"-2355px","left":"150px"});
          slider();  
        });
    });
        
        function slider(){
            
            
         $(".a2").animate({opacity:'1'},2000);
        $(".a1").animate({opacity:'1'},4000,function(){
           $(".a3").animate({opacity:'1'},2000,function(){$(".a1").css({"-webkit-animation":"rotate 5s infinite linear","animation":"rotate 5s infinite linear"});
            $(".a1").animate({width:'100px',top:'190px'},1000);
            $(".a2").animate({width:'88px',top:'296px'},1000);
            $(".a3").animate({top:'25px',left:'390px',fontSize:'30px'},1000,function(){
            $(".a19").css("opacity","1");
                 $(".a16").css("opacity","1");
                 $(".a17").css("opacity","1");
                 $(".a18").css("opacity","1");
                $(".a8").css("opacity","1");
                 $(".a9").css("opacity","1");
                 $(".a10").css("opacity","1");
                 $(".a11").css("opacity","1");
                $(".a4").animate({opacity:'1'},1000,function(){
                    $(".a4").animate({opacity:'0'});
                   $(".a7").animate({opacity:'1'},1000,function(){
                       $(".a7").animate({opacity:'0'});
                        $(".a5").animate({opacity:'1'},1000,function(){
                             $(".a5").animate({opacity:'0'});
                          $(".a6").animate({opacity:'1'},1000,function(){  
                               $(".a6").animate({opacity:'0'},function(){
                                $(".a4").animate({opacity:'1'},1000,function(){   
                                  $(".a7").animate({opacity:'1'},1000,function(){ 
                                  $(".a5").animate({opacity:'1'},1000,function(){ 
                                   $(".a6").animate({opacity:'1'},1000,function(){
                                   $(".a2").animate({opacity:'0'},500);
                                   $(".a1").animate({opacity:'0'},500,function(){
                                   $(".a20").animate({opacity:'1'},500);    
                                    $(".a21").animate({opacity:'1'},500,function(){
                                        $(".a9").animate({opacity:'0'},1000);
                                         $(".a8").animate({opacity:'0'},1000);
                                        $(".a16").animate({opacity:'0'},1000);
                                         $(".a17").animate({opacity:'0'},1000);
                                        $(".a19").animate({opacity:'0'},1000);
                                         $(".a11").animate({opacity:'0'},1000,function(){
                                          $(".a6").delay(1000).css({'background':'chartreuse'});                                              $(".a7").delay(1000).css({'background':'chartreuse'});                                              
                   $(".a5").delay(1000).css({'background':'chartreuse'});
                                            
                                         $(".a14").delay(1000).animate({opacity:'1'},2000,function(){
                             $(".a14").css({'color':'black'});   
                             $(".a9").delay(3000).animate({opacity:'1'},1000); 
                           $(".a17").delay(3000).animate({opacity:'1'},1000); 
                           $(".a14").delay(3000).animate({opacity:'0'},500,function(){                             $(".a10").animate({opacity:'0'},1000);
                          $(".a18").animate({opacity:'0'},1000);                                                   $(".a7").css({'background':'hotpink'});                                                 $(".a9").delay(1000).animate({top:'-=150',left:'-=350'});                               $(".a17").delay(1000).animate({top:'-=150',left:'-=350'});
                          $(".a4").delay(500).css({"background":"hotpink"});       
                          $(".a6").delay(1000).css({"background":"hotpink"});     
                          $(".a5").delay(1500).css({"background":"hotpink"}); 
                           $(".a13").delay(2000).animate({opacity:'1'},1000,function(){
                            $(".a13").css({"color":"black"});   
                             $(".a13").delay(3000).animate({opacity:'0'},1000,function(){                            $(".a6").delay(500).css({"background":"orange"}); 
                                 $(".a8").animate({opacity:'1'},1000);
                            $(".a16").animate({opacity:'1'},1000,function(){
                              $(".a9").animate({opacity:'0'},1000);
                                $(".a17").animate({opacity:'0'},1000,function(){
                                 $(".a4").delay(500).css({"background":"orange"});       
                          $(".a5").delay(1000).css({"background":"orange"});     
                          $(".a7").delay(1500).css({"background":"orange"}); 
                          $(".a8").animate({left:"+=300px",top:'-=150px'},1000);
                          $(".a16").animate({left:"+=300px",top:'-=150px'},1000,function(){
                           $(".a12").animate({opacity:'1'},1000,function(){
                            $(".a12").css({"color":"black"});    
                                   $(".a12").delay(3000).animate({opacity:'0'},1000,function(){                            $(".a5").delay(500).css({"background":"deepskyblue"}); 
                                 $(".a11").animate({opacity:'1'},1000);
                            $(".a19").animate({opacity:'1'},1000);
                              $(".a8").animate({opacity:'0'},1000);
                                $(".a16").animate({opacity:'0'},1000,function(){
                                 $(".a7").delay(500).css({"background":"deepskyblue"});       
                          $(".a6").delay(1000).css({"background":"deepskyblue"});     
                          $(".a4").delay(1500).css({"background":"deepskyblue"}); 
                          $(".a11").animate({top:'-=350px'},1000);
                          $(".a19").animate({top:'-=350px'},1000,function(){
                           $(".a15").animate({opacity:'1'},1000,function(){
                            $(".a15").css({"color":"black"});  
                           $(".a11").delay(3000).animate({opacity:'0'},1000);
                               $(".a15").delay(3000).animate({opacity:'0'},1000);
                               $(".a19").delay(3000).animate({opacity:'0'},1000,function(){
                          $(".a6").css({"background":"#4f4f4f"},1000);     
                          $(".a4").css({"background":"#4f4f4f"},1000); 
                          $(".a7").css({"background":"#4f4f4f"},1000);     
                          $(".a5").css({"background":"#4f4f4f"},1000); 
                                   $(".a22").animate({opacity:"1"},1000,function(){
                                       $(".a2").animate({opacity:"1"},1000); 
                                       $(".a1").animate({opacity:"1"},1000,function(){
                                          $(".a23").animate({opacity:"1"},1000);   
                                           $(".a24").animate({opacity:"1"},1000);  
                                      
                                       
                                       
});});});});});});});});});});});});});});});});});});});});});});});});});});});});});});
       
        
        
        }