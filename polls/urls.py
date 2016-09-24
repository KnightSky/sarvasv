from django.conf.urls import url, include
from . import views
from polls.views import *
urlpatterns = [
 url('', include('social.apps.django_app.urls', namespace='social')),
 url('', include('django.contrib.auth.urls', namespace='auth')),
 url(r'^home1/$', views.login),
 url(r'^home/$', views.login),
 url(r'^home/dashboard/$', views.dashboard1),
 url(r'^home/dashboard1/$', views.dashboard),
 url(r'^events/selquiz/$', views.selquiz),
 url(r'^register/$', views.register),
 #url(r'^polls_json/$', views.ajax),
 url(r'^register/test/$',views.test),
 url(r'^register/social_auth/$',views.social_auth),
 url(r'^register/QuizReg/EditOrCreate/(?P<quizname>.+)/$',views.quizuptab),
 url(r'^register/QuizReg/Delete/(?P<quizname>.+)/$',views.delref),
 url(r'^register/test2/(?P<quizname>.+)/$',views.editq),
 url(r'^register/test3/(?P<quizname>.+)/$',views.delq),
 url(r'^register/(?P<eid>.+)/(?P<otp>\d+)/$',views.transfer_details),
 url(r'^register/fill_details/$',views.register2),
 url(r'^register/QuizReg/$',views.QuizReg),
 url(r'^register/QuizReg/EditOrCreate/$',views.EditOrCreate),
 url(r'^register/QuizReg/EditOrCreate1/CreateQuiz/$',views.CreateQuiz),
 url(r'^events/selquiz/desc/register/(?P<quizname>.+)/$',views.UserQuizReg),
 url(r'^events/selquiz/desc/(?P<quizname>.+)/$',views.RegCheck),
 url(r'^events/selquiz/quiz/QuizPlay/Score/(?P<quizname>.+)/$',views.Score),
 url(r'^events/selquiz/quiz/QuizPlay/(?P<quizname>.+)/$',views.QuizPlay),
 url(r'^events/selquiz/quiz/(?P<quizname>.+)/$',views.quizgo),
 url(r'^QuizReg/EditOrCreate/editdetails/$',views.ChangeDate),
 url(r'^QuizReg/EditOrCreate/editques/(?P<quizname>.+)/$',views.editref)
]
