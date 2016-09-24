from django import forms
from polls.models import Users,UserProfile


class UserForm(forms.ModelForm):
    college = forms.CharField(max_length=120)
    emailid = forms.EmailField()
    password = forms.PasswordInput()
    conpassword=forms.PasswordInput()
    username=forms.CharField(max_length=100)

    class Meta:
        model=Users
        fields=('college','emailid','password','conpassword','username')



class UserProfileForm(forms.ModelForm):
     firstname = forms.CharField(max_length=60)
     lastname = forms.CharField(max_length=60)
     dob = forms.DateField()
     gender = forms.CharField(max_length=2)
     fathername = forms.CharField(max_length=60)
     permaadd = forms.CharField(max_length=200)
     contact = forms.CharField(max_length=11)
     #profilepic=forms.ImageField()
     picture = forms.ImageField()


     class Meta:
         model=UserProfile
         fields=('firstname','lastname','dob','gender','fathername','permaadd','contact','picture')




class InterestsForm(forms.ModelForm):
     interest1=forms.NullBooleanField()
     interest2=forms.NullBooleanField()
     interest3=forms.NullBooleanField()
     interest4=forms.NullBooleanField()
     interest5=forms.NullBooleanField()

     class Meta:
         model=UserProfile
         fields=('interest1','interest2','interest3','interest4','interest5')

class Quizm(forms.ModelForm):
    ques=forms.CharField(max_length=5000)
    o1=forms.CharField(max_length=1000)
    o2=forms.CharField(max_length=1000)
    o3=forms.CharField(max_length=1000)
    o4=forms.CharField(max_length=1000)
    o5=forms.CharField(max_length=1000)
    o6=forms.CharField(max_length=1000)
    o7=forms.CharField(max_length=1000)
    o8=forms.CharField(max_length=1000)
    o9=forms.CharField(max_length=1000)
    o10=forms.CharField(max_length=1000)
    c1=forms.CheckboxInput()
    c2=forms.CheckboxInput()
    c3=forms.CheckboxInput()
    c4=forms.CheckboxInput()
    c5=forms.CheckboxInput()
    c6=forms.CheckboxInput()
    c7=forms.CheckboxInput()
    c8=forms.CheckboxInput()
    c9=forms.CheckboxInput()
    c10=forms.CheckboxInput()
