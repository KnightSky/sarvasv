from django.core.mail import send_mail,EmailMessage
import sqlite3
from polls.registerform import UserForm
import random
from django.core.mail import EmailMultiAlternatives
from polls.models import Users



def mail(eid):
   subject, from_email, to = 'hello', 'solankiarnav123@gmail.com', eid
   text_content = 'This is an important message.'
   otp=random_num()
   otpstr=str(otp)
   print(otp)
   html_content = '<p><a  href="http://127.0.0.1:8000/polls/register/'+eid+'/'+otpstr+'/" ><strong>Here is your link to the next page</strong></a></p>'
   msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
   msg.attach_alternative(html_content,"text/html")
   t=msg.send()
   dict={'t':t,'otpstr':otpstr}
   return dict

def mail2(eid,quizname):
   #email = EmailMessage('Subject','otp', to=[eid])
   subject, from_email, to = 'hello', 'solankiarnav123@gmail.com', eid
   text_content = 'This is an important message.'
   html_content = '<p><a><strong>You have successfully registered for the quiz'+quizname+'</strong></a></p>'
   msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
   msg.attach_alternative(html_content, "text/html")
   t=msg.send()
   return 0

def tablechk(tabname,field1,var):

   conn=sqlite3.connect('db.sqlite3')
   cursor=conn.cursor()
   cursor.execute(" Select Count (*) from "+tabname+" where "+field1+" =?",(var,))
   conn.commit()
   chkvar=cursor.fetchone()
   cursor.close()
   print (""+str(chkvar[0]))
   if chkvar[0]==0 :
       return 1
   else :
       return 0

def intrchk(formint):
    if(formint=='1'):
        return None
    elif(formint=='2'):
        return 1
    elif(formint=='3'):
        return 0
#def mail(UserForm):
       # u=send_mail('subject','message','from@example.com',[UserForm],fail_silently=False,auth_user=None,auth_password=None,connection=None,html_message=None)
        #return u

def random_num():
    return random.randint(100000,999999)




