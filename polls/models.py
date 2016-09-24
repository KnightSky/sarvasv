from django import forms
from django.db import models
import django.dispatch
sentdata=django.dispatch.Signal(providing_args=["arg"])

class UserProfile(models.Model):
     firstname = models.CharField(max_length=60,null=True,blank=True)
     dob = models.DateField(null=True,blank=True)
     contact = models.CharField(max_length=11,null=True,blank=True)
     college = models.CharField(max_length=120,null=True,blank=True)
     emailid = models.EmailField()
     username=models.CharField(max_length=200)
     password = models.CharField(max_length=20,blank=True,null=True)
     picture=models.ImageField(upload_to='profile_images', blank=True, null=True)

class Global(models.Model):
    username=models.CharField(max_length=200,blank=True)
    emailid=models.EmailField()
    sessionid=models.CharField(max_length=1000,blank=True)

class Users(models.Model):
    college = models.CharField(max_length=120)
    emailid = models.EmailField()
    password = models.CharField(max_length=20,blank=True,null=True)
    conpassword=models.CharField(max_length=20,blank=True,null=True)
    username=models.CharField(max_length=200)
    otp=models.CharField(max_length=20,blank=True)
    name=models.CharField(max_length=200,default='none')

#class Dummy(models.Model):
    #dummydata=models.CharField(max_length=10)
    #def send_data(self):
       # sentdata.send(sender=self._class_,arg="True")

class ProfilePicture(models.Model):
    emailid = models.CharField(max_length=60, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, null=True)
    def __unicode__(self):
        return self.emailid

class QuizReg(models.Model):
    loginid=models.CharField(max_length=1000,blank=False,null=False)
    passwd=models.CharField(max_length=1000,blank=False,null=False)

class QuizGlobal(models.Model):
    creator=models.CharField(max_length=1000,blank=False,null=False)
    quizname=models.CharField(max_length=5000,blank=False,null=False)
    starttime=models.DateTimeField(blank=True, null=True)
    endtime=models.DateTimeField(blank=True, null=True)
    duration=models.IntegerField(blank=True, null=True)
    description=models.CharField(max_length= 10000, blank=True, null=True)
    marking=models.CharField(max_length= 10000, blank=True, null=True)
    prizes=models.CharField(max_length= 10000, blank=True, null=True)
    mscc=models.IntegerField(blank=True, null=True)
    msci=models.IntegerField(blank=True, null=True)
    mmcc=models.IntegerField(blank=True, null=True)
    mmci=models.IntegerField(blank=True, null=True)
    minputypecorrect=models.IntegerField(blank=True,null=True)
    minputypeincorrect=models.IntegerField(blank=True,null=True)