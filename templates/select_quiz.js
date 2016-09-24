
function quizlist1(n1)
{$(document).ready(function(){
	 var i;
    for(i=0;i<n1;i++)
    {
    $("div.fake1").append('<div class="list"><span><a href="www.facebook.com">Quiz'+(i+1)+'</a></span></div>'); 
    }
});
}
quizlist1(6);

	
function quizlist2(n2)
{$(document).ready(function(){
	 var i;
    for(i=0;i<n2;i++)
    {
    $("div.fake2").append('<div class="list"><span><a href="www.youtube.com">Quiz'+(i+1)+'</a></span></div>'); 
    }
});
}
quizlist2(2);

	