from django.conf.urls import url
from . import views
from polls.views import *
urlpatterns = [
 url(r'^register/$', views.register),
 url(r'^polls_json/$', views.ajax),
 url(r'^register/test/$',views.quizcrtab),
 url(r'^register/test1/$',views.quizuptab),
 url(r'^register/test2/$',views.editq),
 url(r'^register/(?P<eid>.+)/(?P<otp>\d+)/$',views.transfer_details),
 url(r'^register/(?P<eid>.+)/(?P<otp>\d+)/interests/$',views.register2),
 url(r'^register/(?P<eid>.+)/(?P<otp>\d+)/interests/dashboard/$',views.register3),
]