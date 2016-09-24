from django import forms
from django.db import models
import django.dispatch
sentdata=django.dispatch.Signal(providing_args=["arg"])

class UserProfile(models.Model):
     firstname = models.CharField(max_length=60,null=True,blank=True)

     lastname = models.CharField(max_length=60 ,null=True,blank=True)
     dob = models.DateField(null=True,blank=True)
     gender = models.CharField(max_length=2,null=True,blank=True)
     fathername = models.CharField(max_length=60,null=True,blank=True)
     permaadd = models.CharField(max_length=200,null=True,blank=True)
     contact = models.CharField(max_length=11,null=True,blank=True)
     college = models.CharField(max_length=120)
     emailid = models.EmailField()
     username=models.CharField(max_length=200)
     password = models.CharField(max_length=20)
     interest1 = models.NullBooleanField(default=False)
     interest2 = models.NullBooleanField(default=False)
     interest3 = models.NullBooleanField(default=False)
     interest4 = models.NullBooleanField(default=False)
     interest5 = models.NullBooleanField(default=False)
     picture=models.ImageField(upload_to='profile_images', blank=True, null=True)

class Global(models.Model):
    username=models.CharField(max_length=200,blank=True)
    emailid=models.EmailField()
    sessionid=models.CharField(max_length=10000,blank=True)
    is_loggedin=models.BooleanField(default=False)

class Users(models.Model):
    college = models.CharField(max_length=120)
    emailid = models.EmailField()
    password = models.CharField(max_length=20)
    conpassword=models.CharField(max_length=20)
    username=models.CharField(max_length=200)
    otp=models.CharField(max_length=20,blank=True)

#class Dummy(models.Model):
    #dummydata=models.CharField(max_length=10)
    #def send_data(self):
       # sentdata.send(sender=self._class_,arg="True")

class ProfilePicture(models.Model):
    emailid = models.CharField(max_length=60, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_images', blank=True, null=True)
    def __unicode__(self):
        return self.emailid

class Question(models.Model):
    qid=models.CharField(max_length=8,blank=False, null=False)
    questionText=models.CharField(max_length=5000,blank=False,null=False)
    option1Text=models.CharField(max_length=500,blank=True,null=True)
    option2Text=models.CharField(max_length=500,blank=True,null=True)
    option3Text=models.CharField(max_length=500,blank=True,null=True)
    option4Text=models.CharField(max_length=500,blank=True,null=True)
    option5Text=models.CharField(max_length=500,blank=True,null=True)
    option6Text=models.CharField(max_length=500,blank=True,null=True)
    option7Text=models.CharField(max_length=500,blank=True,null=True)
    option8Text=models.CharField(max_length=500,blank=True,null=True)
    option9Text=models.CharField(max_length=500,blank=True,null=True)
    option10Text=models.CharField(max_length=500,blank=True,null=True)
    answerSeq=models.CharField(max_length=10,blank=False,null=False)

