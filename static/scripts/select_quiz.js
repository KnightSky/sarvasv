var xyz=['2_aug_16 ','3_aug_16','1_aug_16'];
function quizlist1(n1,xyz)
{$(document).ready(function(){
	 var i;
    for(i=0;i<n1;i++)
    {
    $("div.fake1").append('<div class="list"><a href="www.facebook.com"><span>Quiz'+(i+1)+'<br><b>Held</b>:&nbsp '+xyz[i]+'</span></a></div>'); 
    }
});
}
quizlist1(16,xyz);

	
function quizlist2(n2,xyz)
{$(document).ready(function(){
	 var i;
    for(i=0;i<n2;i++)
    {
    $("div.fake2").append('<div class="list"><a href="www.youtube.com"><span>Quiz'+(i+1)+'<br><b>Upcoming</b>: &nbsp'+xyz[i]+'</span></a></div>'); 
    }
});
}
quizlist2(8,xyz);

	