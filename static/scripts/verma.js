
function quizlist(n)
{$(document).ready(function(){
	 var i;
    for(i=0;i<n;i++)
    {
    $("div.fake").append('<div class="listq"><span><a href="www.facebook.com">Quiz'+(i+1)+'</a></span></div>'); 
    }
});
}
quizlist(15);

	