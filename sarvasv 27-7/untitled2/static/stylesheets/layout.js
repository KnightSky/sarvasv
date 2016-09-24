
 var t=true;
var mha=true;
var st=false;
var sx=window.innerWidth;
var left;
var cs=0;
var ele=[];
if(sx>960) left=300;
else if(sx>600)left =200;
else left=0;
$(document).ready(function(){
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
                 $(this).css({"-ms-transform":"rotate(180deg)","-webkit-transform":"rotate(180deg)","transform":"rotate(180deg)"});
                $('.bodyc').css('display','none');
                 
            }
            else{
    $(this).css({"-ms-transform":"rotate(180deg)","-webkit-transform":"rotate(180deg)","transform":"rotate(180deg)"});
        $(".bodyc").animate({
            left: '+='+left+'px',
        width: '-='+left+'px'
        });
                
       } t=false;}
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
  
       

    //Registration
    $('#id_password').keyup(function(){
         if($('#id_conpassword').val()!="")
        { 
   if($('#id_conpassword').val()!=$('#id_password').val()) {
       $('.rmsg').text("Password do not match!").animate({opacity:'1'}); 
       mha=false;
   }else{
        $('.rmsg').text("").animate({opacity:'0'}); 
   }
        }
    });
    $('#id_conpassword').keyup(function(){
   if($('#id_conpassword').val()!=$('#id_password').val()) {
       $('.rmsg').text("Password do not match!").animate({opacity:'1'}); 
   }else{
        $('.rmsg').text("").animate({opacity:'0'}); 
   }
    });
     
    
    
       var iiu=0;

    $(".btn").click(function()
    {
        var mail = $('.form>input[name=email]').val();
                                var atposmail = mail.indexOf("@");
                                var dotposmail = mail.lastIndexOf(".");
                                var spacemail = mail.indexOf(" ");
                                var username = $('.form>input[name=UserName]').val();
                                if (iiu == 0) {
                                    //Username
                                    if (username == "" || username.indexOf("@") != -1) {
                                        $('.rmsg').text("Please Enter Your User Name").animate({opacity: '1'});
                                        $('.form>input[name=UserName]').focus();
                                        mha = false;

                                    }
                                    //email
                                    else if (atposmail < 1 || dotposmail < atposmail + 2 || dotposmail + 2 >= mail.length || spacemail != -1) {
                                        $('.rmsg').text("Blank or Invalid Email Id").animate({opacity: '1'});
                                        $('.form>input[name=email]').focus();
                                        mha = false;
                                    }
                                    //password
                                    else if ($('.form>input[name=password]').val().length < 7 || $('.form>input[name=password]').val().length > 20) {
                                        $('.rmsg').text("length must be in between 8 to 20").animate({opacity: '1'});
                                        $('.form>input[name=password]').focus();
                                        mha = false;
                                    }
                                    //confirm password
                                    else if ($('.form>input[name=cpassword]').val() == "") {
                                        $('.rmsg').text("Password do not match!!").animate({opacity: '1'});
                                        $('.form>input[name=cpassword]').focus();
                                        mha = false;
                                    }
                                    //all ok
                                    else {
                                        mha = true;
                                        $('.rmsg').text("").animate({opacity: '0'});
                                    }
                                }
        });
        $(".btn2").click(function()
    {
            if(iiu==1)
                  {
    var cno=$('.form>input[name=contactno]').val();
    var pcode=$('.form>input[name=pincode]').val();
                      //name
        if( $('.form>input[name=firstname]').val()=="")
         {

           $('.rmsg').text("Please Tell Your Name").animate({opacity:'1'});
             $('.form>input[name=firstname]').focus() ;
            mha=false;

         }

        else if($('.form>input[name=fathername]').val()=="")
         {
           $('.rmsg').text("Please Enter Your Father's Name").animate({opacity:'1'});
            $('.form>input[name=fathername]').focus() ;
            mha=false;

         }
        else if($('.form>input[name=address]').val()=="")
         {
           $('.rmsg').text("Please tell your address so that we can send your prize!!").animate({opacity:'1'});
            $('.form>input[name=address]').focus() ;
            mha=false;
         }

        else if(pcode.length==5||pcode==""||pcode.indexOf("-")!=-1)
         {
           $('.rmsg').text("Blank or Invalid pin code!!").animate({opacity:'1'});
            $('.form>input[name=pincode]').focus() ;
            mha=false;

         }

            else if(cno.length>13||cno==""||cno.indexOf("-")!=-1)
         {
           $('.rmsg').text("Your Contact is important to us :)").animate({opacity:'1'});
            $('.form>input[name=contactno]').focus() ;
            mha=false;
                  }
            else{
                 mha=true;
                $('.rmsg').text("").animate({opacity:'0'});
                alert("hello");
            }

         }

        });
$(".btn2").click(function(){
          document.getElementById("fform").submit();
    });
});
