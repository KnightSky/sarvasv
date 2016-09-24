
$(document).ready(function(){
	
	$(".instructions>a>div").click(function(){
	
		if($(".instructions>a>div").eq(0).hasClass("jbyy")){
$(".instructions>a>div").eq(0).removeClass("jbyy");
	}if($(".instructions>a>div").eq(1).hasClass("jbyy")){
$(".instructions>a>div").eq(1).removeClass("jbyy");
	}if($(".instructions>a>div").eq(2).hasClass("jbyy")){
$(".instructions>a>div").eq(2).removeClass("jbyy");
	}if($(".instructions>a>div").eq(3).hasClass("jbyy")){
$(".instructions>a>div").eq(3).removeClass("jbyy");
	}
		$(this).addClass("jbyy");
		
	});
	$("#enter_quiz").click(function(){
	
		if($(".h_cb").prop("checked")){
			window.open("url","_self");
			}else{
				alert("Please ");
			}
		});
	
	
});


$(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});
