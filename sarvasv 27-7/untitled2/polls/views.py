from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import sqlite3
from polls.registerform import UserForm,UserProfileForm,InterestsForm
from polls.misc_functions import mail,random_num, tablechk, intrchk
from polls.models import ProfilePicture,UserProfile
import json,datetime
from django.contrib.sessions.models import Session
import time
from django.db.models.signals import post_save
from django.dispatch import receiver

otp=0
Response=''





def register(request):
   registered = False


   # If it's a HTTP POST, we're interested in processing form data
   print('chk0')
   if request.method == 'POST':
     if request.POST.get('emailid')!='0':
      eidstr= request.POST.get('emailid')
     else:
      eidstr= request.POST.get('emailid2')
     vara= tablechk('polls_userprofile','emailid', eidstr )
     if(vara==1):

       print("alpha"+str(vara))
       if request.POST.get('emailid')!='0':
         ajaxstr='chk1'
        # print(ajaxstr)
         user_form = UserForm(data=request.POST)

        # print('chk2')
         response_dict={}


         if request.POST.get('password') == request.POST.get('conpassword'):

              if vara==1:

                   print("kutta")
                   otpstr=mail(request.POST.get('emailid'))

                   message='mail sent'
                   str1= request.POST.get('emailid')
                   print("ert"+otpstr+str1)


                   # Save the user's form data to the database.
                   user = user_form.save()
                   # Now we hash the password with the set_password method.
                   # Once hashed, we can update the user object.
                   #user.password(user.password)
                   user.save()
                   conn = sqlite3.connect('db.sqlite3')
                   cursor=conn.cursor()
                   cursor.execute('''UPDATE polls_users SET otp = ? where emailid = ? ''',(otpstr,str1))
                   cursor.close()
                   conn.commit()
                   ajaxstr="Email sent"
                   registered= True
                   response_dict.update({'resp1' : ajaxstr, 'gamma' : 0})

                   return HttpResponse(json.dumps(response_dict),content_type='application/javascript')

              else:
                   ajaxstr='Email id already registered'
                   response_dict.update({'resp1' : ajaxstr,'gamma':0})
                   return HttpResponse(json.dumps(response_dict))
         else:
               return HttpResponse("Password don't match")

       else :
          response_dict={}
          gamma=0
          response_dict.update({'gamma':gamma, 'resp1': 'Email has been sent'})
          return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
     else:
         response_dict={}
         gamma=1
         if(request.POST.get('emailid')==request.POST.get('emailid2')):
           response_dict.update({'gamma':gamma, 'resp1': 'Email id already registered'})
         else :
           response_dict.update({'gamma':gamma, 'resp1': 'Chal gaya', })
         return HttpResponse(json.dumps(response_dict),content_type='application/javascript')

   # Not a HTTP POST, so we render our form using two ModelForm instances.
   # These forms will be blank, ready for user input.
   else:
       user_form = UserForm()
       user_profileform = UserProfileForm()
       ajaxstr='Email has been sent4545'
       print(ajaxstr)

       # Render the template depending on the context.
       return render_to_response('polls/registerform.html',{'user_form': user_form,'user_profileform' : user_profileform ,'registered':registered},context_instance=RequestContext(request))

def ajax(request):
     if ('client_response') in request.POST:
        x = request.POST['client_response']
        if(otp==int(x)):
           # print (otp)
            Response='True'
        else:
            Response='False'

        response_dict = {'Response':Response}
        return HttpResponse(json.dumps(response_dict), content_type='application/javascript')
     else:
        return render_to_response('registerform.html', context_instance=RequestContext(request))

def transfer_details(request,eid,otp):

     conn = sqlite3.connect('db.sqlite3')
     cursor=conn.cursor()
     cursor.execute('''Select emailid from polls_users where emailid = ? and otp = ?''',(eid,otp))
     conn.commit()
     emailid_final=cursor.fetchone()
     cursor.execute('''Select password from polls_users where emailid = ? and otp = ?''',(eid,otp))
     conn.commit()
     password_final=cursor.fetchone()
     cursor.execute('''Select college from polls_users where emailid = ? and otp = ?''',(eid,otp))
     conn.commit()
     college_final=cursor.fetchone()
     cursor.execute('''Select username from polls_users where emailid = ? and otp = ?''',(eid,otp))
     username_final=cursor.fetchone()
     conn.commit()
     cursor.execute('''DELETE FROM polls_users where emailid = ?''', (eid,))
     conn.commit()


     cursor.execute('''INSERT INTO polls_userprofile (emailid, password, college,username) values(?,?,?,?)''',(emailid_final[0],password_final[0],college_final[0],username_final[0]))
     conn.commit()
     # if request.session.get('last_visit'):
     #
     #          # The session has a value for the last visit
     #   last_visit_time = request.session.get('last_visit')
     #   visits = request.session.get('visits', 0)
     #   if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
     #     request.session['visits'] = visits + 1
     #     request.session['last_visit'] = str(datetime.now())
     #   new_sessionid=request.session._get_new_session_key()
     #   cursor.execute('''INSERT INTO polls_global (emailid, username, sessionid,is_loggedin) values(?,?,?,?)''',(emailid_final[0],username_final[0],new_sessionid ,True))


   #  else:
        # The get returns None, and the session does not have a value for the last visit.
     request.session['last_visit'] = str(time.strftime("%H:%M:%S"))
     request.session['visits'] = 1
     request.session['eid']=eid
     request.session['otp']=otp
     new_sessionid=request.session._get_new_session_key()
     cursor.execute('''INSERT INTO polls_global (emailid, username, sessionid,is_loggedin) values(?,?,?,?)''',(emailid_final[0],username_final[0],new_sessionid ,True))
     conn.commit()
     user_profileform= UserProfileForm()
     #if request.session.has_key('last_visit'):

     return render_to_response('polls/registerform.html',{'user_form': user_profileform, 'eid' : eid, 'otp' : otp},context_instance=RequestContext(request))



def register2(request,eid,otp):
    if request.method=='POST':
        userprofile_form=UserProfileForm(request.POST, request.FILES)
        if userprofile_form.is_valid():
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            dob=request.POST['dob']
            gender=request.POST['gender']
            fathername=request.POST['fathername']
            permaadd=request.POST['permaadd']
            contact=request.POST['contact']
            if 'picture' in request.FILES:
               userprofile_form.picture=request.FILES['picture']

            new=ProfilePicture(emailid=eid, picture=userprofile_form.picture)
            new.save()
            conn = sqlite3.connect('db.sqlite3')
            cursor=conn.cursor()
            cursor.execute('''UPDATE polls_userprofile SET firstname=? , lastname=? ,dob=?, gender=?,fathername=?,permaadd=?,contact =?  where emailid = ? ''',(firstname,lastname,dob,gender,fathername,permaadd,contact,eid,))
            print ('alpha')
            conn.commit()
            interest_form=InterestsForm()
            return render_to_response('polls/interestform.html',{'interest_form': interest_form, 'eid' : eid, 'otp' : otp},context_instance=RequestContext(request))

        else:
           # Invalid form or forms - mistakes or something else?
           # Print problems to the terminal.
           # They'll also be shown to the user.        
            return HttpResponse(userprofile_form.errors)

    else:
            userprofile_form = UserProfileForm()

       # Render the template depending on the context.
            return render_to_response('polls/userprofileform.html',{'userprofile_form': userprofile_form},context_instance=RequestContext(request))



def register3(request,eid,otp):
     if request.method=='POST':
         interest_form=InterestsForm(data=request.POST)
         if interest_form.is_valid():
             interest1=request.POST['interest1']
             interest2=request.POST['interest2']
             interest3=request.POST['interest3']
             interest4=request.POST['interest4']
             interest5=request.POST['interest5']
             interest1=str(interest1)
             interest2=str(interest2)
             interest3=str(interest3)
             interest4=str(interest4)
             interest5=str(interest5)
             conn=sqlite3.connect('db.sqlite3')

             cursor=conn.cursor()
             cursor.execute('''UPDATE polls_userprofile SET interest1=?,interest2=?,interest3=?,interest4=?,interest5=? where emailid=? ''',(intrchk(interest1),intrchk(interest2),intrchk(interest3),intrchk(interest4),intrchk(interest5),eid,))
             conn.commit()

             return HttpResponse(" "+str(interest1))
         else :
             return HttpResponse(interest_form.errors)

     else:
            interest_form=InterestsForm()




       # Render the template depending on the context.
            return render_to_response('polls/interestform.html',{'interest_form': interest_form},context_instance=RequestContext(request))

def func1(request):
  conn=sqlite3.connect('db.sqlite3')
  cursor=conn.cursor()
  cursor.execute('''UPDATE polls_userprofile set interest1=? where emailid=?''',(intrchk(1),'vsandstorm0@gmail.com',))
  conn.commit()

  return HttpResponse("qwe")

def test(request):
    return render_to_response('polls/quizm.htm',context_instance=RequestContext(request))

def quizcrtab(request):
    conn=sqlite3.connect('db.sqlite3')
    cursor=conn.cursor()
    cursor.execute('''CREATE TABLE quiz2 (
    quesno INTEGER PRIMARY KEY AUTOINCREMENT,
    ques TEXT NOT NULL,
    options INTEGER NOT NULL,
    opt1 TEXT NOT NULL,
    opt2 TEXT NOT NULL,
    opt3 TEXT NOT NULL,
    opt4 TEXT NOT NULL,
    opt5 TEXT NOT NULL,
    opt6 TEXT NOT NULL,
    opt7 TEXT NOT NULL,
    opt8 TEXT NOT NULL,
    opt9 TEXT NOT NULL,
    opt10 TEXT NOT NULL,
    ans TEXT NOT NULL
    )''')
    conn.commit()

    return HttpResponse("qwe")

def quizuptab(request):
    if(request.method=='POST'):
        ques=request.POST['ques']
        options=request.POST['nq']
        opt1=request.POST['o1']
        opt2=request.POST['o2']
        opt3=request.POST['o3']
        opt4=request.POST['o4']
        opt5=request.POST['o5']
        opt6=request.POST['o6']
        opt7=request.POST['o7']
        opt8=request.POST['o8']
        opt9=request.POST['o9']
        opt10=request.POST['o10']
        c1=request.POST.get('c1',0)
        c2=request.POST.get('c2',0)
        c3=request.POST.get('c3',0)
        c4=request.POST.get('c4',0)
        c5=request.POST.get('c5',0)
        c6=request.POST.get('c6',0)
        c7=request.POST.get('c7',0)
        c8=request.POST.get('c8',0)
        c9=request.POST.get('c9',0)
        c10=request.POST.get('c10',0)
        if(c1!=0):
            c1='1'
        if(c2!=0):
            c2='1'
        if(c3!=0):
            c3='1'
        if(c4!=0):
            c4='1'
        if(c5!=0):
            c5='1'
        if(c6!=0):
            c6='1'
        if(c7!=0):
            c7='1'
        if(c8!=0):
            c8='1'
        if(c9!=0):
            c9='1'
        if(c10!=0):
            c10='1'
        ans=str(c1)+str(c2)+str(c3)+str(c4)+str(c5)+str(c6)+str(c7)+str(c8)+str(c9)+str(c10)
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        print("chala")
        cursor.execute('''INSERT INTO quiz2 (ques,options,opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10,ans) values(?,?,?,?,?,?,?,?,?,?,?,?,?)''',(ques,options,opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10,ans))
        conn.commit()
        cursor.execute('''Select ques from quiz2 ''')
        conn.commit()
        qarray=cursor.fetchall()

        tabname='quiz2'
        cursor.execute(" Select Count (*) from "+tabname)
        conn.commit()
        up=cursor.fetchone()
        i=[0]*up[0]
        arrayq=[""]*(up[0]+1)
        print(up[0])
        for k in range(0,up[0]):
            arrayq[k]=qarray[k][0]
            i[k]=k
        return render_to_response('polls/quizm.htm',{"qarray":arrayq,"limits":i,"up":up[0]},context_instance=RequestContext(request))
        #return HttpResponse("Baad diya")


    else:
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        cursor.execute('''Select ques from quiz2 ''')
        conn.commit()
        qarray=cursor.fetchall()
        tabname='quiz2'
        cursor.execute(" Select Count (*) from "+tabname)
        conn.commit()
        up=cursor.fetchone()
        i=[0]*up[0]
        arrayq=[""]*(up[0]+1)
        #print(up[0])
        for k in range(0,up[0]):
            arrayq[k]=qarray[k][0]
            i[k]=k
        #print(arrayq[1][0])
        return render_to_response('polls/quizm.htm',{"qarray":arrayq,"limits":i,"up":up[0]},context_instance=RequestContext(request))
        #return render_to_response('polls/quizm.htm',context_instance=RequestContext(request))


def editq(request):
    if(request.method=="POST"):
        pry=request.POST.get("qid")
        pry1=pry[1:]
        pry2=int(pry1)+1
        print(pry2)
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        cursor.execute('''Select ques from quiz2 where quesno = ?''',(pry2,) )
        conn.commit()
        quesa=cursor.fetchone()
        ques=quesa[0]
        option=[""]*11
        cursor.execute('''Select opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10 from quiz2 where quesno = ?''',(pry2,) )
        conn.commit()
        clap=cursor.fetchall()
        print(clap[0][1])
        for i in range(1,11):
            option[i]=clap[0][i-1]
        cursor.execute('''Select options from quiz2 where quesno = ?''',(pry2,) )
        conn.commit()
        print(option)
        noptionsa=cursor.fetchone()
        noptions=noptionsa[0]
        cursor.execute('''Select ans from quiz2 where quesno = ?''',(pry2,) )
        conn.commit()
        ansa=cursor.fetchone()
        ans=ansa[0]
        print(ans)
    response_dict={}
    #response_dict.update({'ques':ques,'id':pry2, 'noptions':noptions, 'ans':ans,'opt1': option[1], 'opt2': option[2], 'opt3': option[3], 'opt4': option[4], 'opt5': option[5], 'opt6': option[6], 'opt7': option[7], 'opt8': option[8], 'opt9': option[9], 'opt10': option[10], })
    response_dict.update({'ques':ques,'id':pry2, 'noptions':noptions, 'ans':ans, 'option': option})
    return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
