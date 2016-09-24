
 var t=true;
var st=false;
var sx=window.innerWidth;
var left;
var cs=0;
var ele=[];
var winlength =($(window).height())/2-200;//provide the vertical margin to loader.
var pagelength = $(document).height();  



if(sx>960) left=300;
else if(sx>600)left =200;
else left=0;

$(document).ready(function(){
    //meassage
       
        $('.closingmessage').click(function(){
            message("0");
        });
    
    //menu
     $(".bodym>ul>li>span").click(function(){
        $(this).toggleClass("minus");
        $(this).next().slideToggle("slow"); 
    });

    //Image
    
    $(".imghover>img").hover(function(){
  $(this).next().css("width",""+$(this).width()+"px");
    $(this).parent().css("width",""+$(this).width()+"px");
   
    $(this).parent().css("box-shadow","0 0 4px black");
    $(this).next().css("opacity","1");
   $(this).next().animate({fontSize:'18px'},'fast');
         
    }, function(){
    
   $(this).next().animate({fontSize:'0',opacity:'0'},'slow');
         $(this).parent().css("box-shadow","none");
    }); 
    
  //loader
    
 


  //header-hover
    $(".header2").hover(function(){
    $(".logo2").addClass("rotate");
    $(".glare").css("visibility","visible").animate({left:'100%'},'slow');
},function(){
    if(st){ $(".searchb").animate({width:'0px'}).css("visibility","hidden");  st=false;}
    $(".logo2").removeClass("rotate");
    $(".glare").css("visibility","hidden").animate({left:'0px'},'fast');
}); 
    //search-bar
    $(".search").mouseenter(function(){
        st=true;
    $(".searchb").css("visibility","visible").animate({width:'200px'}).focus();
    });
   //menu
      $(".arrow").click(function(){
        if(t){
            if(left==0){
              //   $(this).css({"-ms-transform":"rotate(180deg)","-webkit-transform":"rotate(180deg)","transform":"rotate(180deg)"});
                $('.bodyc').css('display','none');
            }
            else{
  //  $(this).css({"-ms-transform":"rotate(180deg)","-webkit-transform":"rotate(180deg)","transform":"rotate(180deg)"});
        $(".bodyc").animate({
            left: '+='+left+'px',
        width: '-='+left+'px'
        });
       } 
          $(".logo1").css({
               "-webkit-animation": "rotate1 0.5s linear ",
    "animation": "rotate1 0.5s linear "
          }); 
            
            t=false;}
        else{
            if(left==0){
                $(this).css({"-ms-transform":"rotate(0deg)","-webkit-transform":"rotate(0deg)","transform":"rotate(0deg)"});
                $('.bodyc').css('display','block');
            }
            else{
    $(this).css({"-ms-transform":"rotate(0deg)","-webkit-transform":"rotate(0deg)","transform":"rotate(0deg)"});
        $(".bodyc").animate({
            left: '-='+left+'px',
        width: '+='+left+'px'
        });
        }
             $(".logo1").css({
               "-webkit-animation": "rotate2 0.5s linear ",
    "animation": "rotate2 0.5s linear "
          }); 
          t=true;   
        }
         
});
     //Log-in 
     $(".rightt").click(function(){
              if(t){
            if(left==0){
                 $('.arrow').css({"-ms-transform":"rotate(180deg)","-webkit-transform":"rotate(180deg)","transform":"rotate(180deg)"});
                $('.bodyc').css('display','none');
            }
            else{
    $('.arrow').css({"-ms-transform":"rotate(180deg)","-webkit-transform":"rotate(180deg)","transform":"rotate(180deg)"});
        $(".bodyc").animate({
            left: '+='+left+'px',
        width: '-='+left+'px'
        });
       } t=false;
 $(".bodym>form>fieldset>input[type='text']").focus();}
          });    
  
       

    //Regestration
    $('#rcpwd').keyup(function(){
   if($('#rcpwd').val()!=$('#rpwd').val()) {   
       $('.rmsg').text("Password do not match!").animate({opacity:'1'}); 
   }else{
        $('.rmsg').text("").animate({opacity:'0'}); 
   }
    });
     $('#rpwd').keyup(function(){
   if($('#rcpwd').val()!=$('#rpwd').val()) {   
       $('.rmsg').text("Password do not match!").animate({opacity:'1'}); 
   }else{
        $('.rmsg').text("").animate({opacity:'0'}); 
   }
    });
    
       var iiu=0;         
    $(".btn").click(function(){
        if(iiu==0)
        {$('.form:nth-child(1)').animate({marginLeft:'-110%'});
         $('.form:nth-child(2)').animate({marginLeft:'0px'});
         iiu=1;}
        else if(iiu==1){
             $('.form:nth-child(2)').animate({marginLeft:'-110%'});
         $('.form:nth-child(3)').animate({marginLeft:'110%'});
            iiu=2;
        }
    });
    $(".profile>div:nth-child(2)").hover(function(){
        
        $(".profile").addClass("tilt1");
    },function(){
         $(".profile").removeClass("tilt1");
        
    });  $(".profile>div:nth-child(3)").hover(function(){
        
        $(".profile").addClass("tilt2");
    },function(){
         $(".profile").removeClass("tilt2");
        
    });  $(".profile>div:nth-child(4)").hover(function(){
        
        $(".profile").addClass("tilt3");
    },function(){
         $(".profile").removeClass("tilt3");
        
    });  $(".profile>div:nth-child(5)").hover(function(){
        
        $(".profile").addClass("tilt4");
    },function(){
         $(".profile").removeClass("tilt4");
        
    });
    //for loader
    $('.border4').css('margin-top',winlength+'px');
    
 
});
 

//loader function
  function loading(load){ 
       if(load==1)
        {
            $('.loaderfade').css('display','block');
            $('.loaderfade').css('height',pagelength+'px');
            $('.border4').animate({opacity:"1"},'slow');
        }
        else
        {
            $('.loaderfade').css('display','none');
            $('.border4').animate({opacity:"0"},'slow');
        }}
//message box function
function message(mtitle,mcontent){
   if(mtitle!="0"){ $(".messagebox").slideDown();
    $(".messagetitle").text(mtitle);
    $(".messagetext").text(mcontent);
    $(".closingmessage").slideDown();
                   alert(mtitle+","+mcontent);
}else{
    $(".messagebox").slideUp();
    $(".messagetitle").text("");
    $(".messagetext").text("");
    $(".closingmessage").slideUp();
    
    
}
}
