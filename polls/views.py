#import pymysql
# Add to your settings file
CONTENT_TYPES = ['image']
# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
MAX_UPLOAD_SIZE = "1048576"#500kb

from django import forms
from _ctypes import sizeof
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
import sqlite3
from polls.registerform import QuizRegForm
from polls.misc_functions import mail,mail2,tablechk
from polls.models import ProfilePicture
import json,datetime
import time,threading
import _thread
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.decorators.cache import never_cache

otp=0
Response=''

#Add to a form containing a FileField and change the field names accordingly.
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
def clean_content(self):
    content = self.cleaned_data['content']
    content_type = content.content_type.split('/')[0]
    if content_type in settings.CONTENT_TYPES:
        if content._size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
    else:
        raise forms.ValidationError(_('File type is not supported'))
    return content


class myThread1(threading.Thread):
    def __init__(self, eid,quizname):
        threading.Thread.__init__(self)
  #      self.threadID = threadID
        self.eid = eid
        self.quizname = quizname
    def run(self):
         mail2(self.eid,self.quizname)
  #      print ("Exiting " + self.name)
#
# def register(request):
#    registered = False
#    # If it's a HTTP POST, we're interested in processing form data
#    print('chk0')
#    if request.method == 'POST':
#              if request.POST.get('emailid')!='0':
#                     eidstr= request.POST.get('emailid')
#                     print("eid"+str(eidstr))
#              else:
#                     eidstr= request.POST.get('emailid2')
#
#              vara= tablechk('polls_userprofile','emailid', eidstr)
#
#              if(vara==1):
#
#                    print("no duplicate email id exists as vara="+str(vara))
#                    if request.POST.get('emailid')!='0':
#                          #ajaxstr='chk1'
#                          print("request.POST.get("+str(request.POST.get('emailid'))+")!=0")
#                          user_form = UserForm(data=request.POST)
#                         # print('chk2')
#                          response_dict={}
#                          if request.POST.get('password') == request.POST.get('conpassword'):
#
#                               if vara==1:
#
#                                        print("kutta")
#                                        otpstr=mail(request.POST.get('emailid'))
#
#                                        message='mail sent'
#                                        str1= request.POST.get('emailid')
#                                        print("ert"+otpstr+str1)
#
#
#                                        # Save the user's form data to the database.
#                                        user = user_form.save()
#                                        # Now we hash the password with the set_password method.
#                                        # Once hashed, we can update the user object.
#                                        #user.password(user.password)
#                                        user.save()
#                                        conn = sqlite3.connect('db.sqlite3')
#                                        cursor=conn.cursor()
#                                        cursor.execute('''UPDATE polls_users SET otp = ? where emailid = ? ''',(otpstr,str1))
#                                        cursor.close()
#                                        conn.commit()
#                                        ajaxstr="Email sent"
#                                        registered= True
#                                        response_dict.update({'resp1' : ajaxstr, 'gamma' : 0})
#
#                                        return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
#                               else:
#                                        ajaxstr='Email id already registered'
#                                        response_dict.update({'resp1' : ajaxstr,'gamma':0})
#                                        return HttpResponse(json.dumps(response_dict))
#                          else:
#                                return HttpResponse("Password don't match")
#
#                    else :
#                           response_dict={}
#                           gamma=0
#                           response_dict.update({'gamma':gamma, 'resp1': 'Email has been sent'})
#                           return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
#              else:
#                  response_dict={}
#                  gamma=1
#                  if(request.POST.get('emailid')==request.POST.get('emailid2')):
#                         response_dict.update({'gamma':gamma, 'resp1': 'Email id already registered'})
#                  else :
#                         response_dict.update({'gamma':gamma, 'resp1': 'Chal gaya', })
#                  return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
#
#    # Not a HTTP POST, so we render our form using two ModelForm instances.
#    # These forms will be blank, ready for user input.
#    else:
#                    user_form = UserForm()
#                    user_profileform = UserProfileForm()
#                #    ajaxstr='Email has been sent4545'
#                    print("request method not post")
#
#                    # Render the template depending on the context.
#                    return render_to_response('polls/registerform.html',{'user_form': user_form,'user_profileform' : user_profileform ,'registered':registered},context_instance=RequestContext(request))

@never_cache
def register(request):
    if(request.method=='POST'):
        eid=request.POST.get('eid')
        uname=request.POST.get('uname')
        clg=request.POST.get('clg')
        pwd=request.POST.get('pwd')
        cpwd=request.POST.get('cpwd')
        name=request.POST.get('name')
        chkeid=tablechk('polls_userprofile','emailid', eid)
        unamechk=tablechk('polls_userprofile','username', uname)
        response_dict={}
        if(chkeid!=1):
            status=1
            return HttpResponse(json.dumps(status),content_type='application/javascript')
        elif(unamechk!=1):
            status=2
            return HttpResponse(json.dumps(status),content_type='application/javascript')
        else:
            dict=mail(eid)
            if(not dict.t):
                status=3
                return HttpResponse(json.dumps(status),content_type='application/javascript')
            elif(dict.t==1):
                conn=sqlite3.connect('db.sqlite3')
                cursor=conn.cursor()
                cursor.execute('''insert into polls_users (name,college,emailid,password,conpassword,username,otp) values(?,?,?,?,?,?)''',(name,clg,eid,pwd,cpwd,uname,dict.otpstr))
                conn.commit()
                status=0
                return HttpResponse(json.dumps(status),content_type='application/javascript')
    else:
        context = RequestContext(request,
        {'request': request,
         'user': request.user})
        return render_to_response('polls/registerform.html',context_instance=context)
#def ajax(request):
#    conn = pymysql.connect(host='localhost', user='root', password='xinjia',
#                 db='db1',charset='utf8mb4',cursorclass=pymysql.cursors.Cursor )
#    cursor=conn.cursor()
#    n=4
#    cursor.execute('''select qno from quiz where qno = ? ''',(n,))
#    conn.commit()
#    n1=cursor.fetchall()
#    return HttpResponse("chala"+str(n1[0][0]))

@never_cache
def transfer_details(request,eid,otp):
     conn = sqlite3.connect('db.sqlite3')
     cursor=conn.cursor()
     cursor.execute('''Select name from polls_users where emailid = ? and otp = ?''',(eid,otp))
     conn.commit()
     name_final=cursor.fetchone()
     emailid_final=cursor.fetchone()
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
     cursor.execute('''INSERT INTO polls_userprofile (firstname,emailid, password, college,username) values(?,?,?,?,?)''',(name_final[0],emailid_final[0],password_final[0],college_final[0],username_final[0]))
     conn.commit()
     cursor.execute('''CREATE TABLE '''+username_final[0]+'''activity (quizname TEXT NOT NULL,starttime DATETIME NOT NULL, endtime DATETIME NOT NULL, points INTEGER NOT NULL, status INTEGER NOT NULL)''')
     conn.commit()
     request.session['eid']=eid
     request.session['otp']=otp
     new_sessionid=request.session._get_new_session_key()
     cursor.execute('''INSERT INTO polls_global (emailid, username, sessionid) values(?,?,?)''',(emailid_final[0],username_final[0],new_sessionid))
     conn.commit()
 #    user_profileform= UserProfileForm()
     output=1
     request.session['uid']=username_final[0]
     return HttpResponse(json.dumps(output),content_type='application/javascript')

@never_cache
def register2(request):
    if request.session.has_key('uid'):
            dob=request.POST.get('dob')
            contact=request.POST.get('contact')
            if 'picture' in request.FILES:
                picture1=request.FILES['image']
            #picture1=clean_content(picture0)
            conn=sqlite3.connect('db.sqlite3')
            cursor=conn.cursor()
            cursor.execute('''select emailid from polls_userprofile where username=?''',(request.session.get('uid'),))
            eid=cursor.fetchone()[0]
            new=ProfilePicture(emailid=eid, picture=picture1)
            new.save()
            conn = sqlite3.connect('db.sqlite3')
            cursor=conn.cursor()
            cursor.execute('''UPDATE polls_userprofile SET dob=?,contact =?  where emailid = ? ''',(dob,contact,eid))
            conn.commit()
            return render_to_response('polls/farzi.html',{'url':"/polls/home/dashboard/"},context_instance=RequestContext(request))
    else:
            return HttpResponse('you are not logged in')

# @never_cache
# def social_login(request):
#     if(request.POST.get('emailid')!=''):
#         name=request.POST.get('name')
#         eid=request.POST.get('emailid')
#         eidchk=tablechk('polls_userprofile','emailid', eid)
#         if(eidchk):
#             return render_to_response('polls/farzi.html',{'url':"/polls/home/dashboard/"},context_instance=RequestContext(request))
#         else:
#             conn=sqlite3.connect('db.sqlite3')
#             cursor=conn.cursor()
#             cursor.execute('''INSERT INTO polls_userprofile (firstname,emailid) VALUES(?,?)''',(name,eid))
#             conn.commit()
#             cursor.execute('''insert into polls_global (emailid) values(?)''',(eid,))
#             conn.commit()
#             request.session['social']=eid
#             return render_to_response('polls/social_login.html',context_instance=RequestContext(request))
#     else:
#         return render_to_response('polls/farzi.html',{'url':"/polls/home/"},context_instance=RequestContext(request))      #######if someone accidentally triggers this view,redirect to home

@never_cache
def social_auth(request):
    if(request.session.has_key('hack')):
        username=request.POST.get('username')
        eid=request.POST.get('eid')
        name=request.POST.get('name')
        uchk=tablechk('polls_userprofile','username',username)
        echk=tablechk('polls_userprofile','emailid',eid)
        if(not echk):
            status=0
            return HttpResponse(json.dumps(status),content_type='application/javascript')
        elif(uchk):
            conn=sqlite3.connect('db.sqlite3')
            cursor=conn.cursor()
            cursor.execute('''insert into polls_userprofile (username,firstname,emailid) values(?,?,?)''',(username,name,eid))
            conn.commit()
            new_sessionid=request.session._get_new_session_key()
            cursor.execute('''update polls_global set sessionid=? where username=?''',(new_sessionid,username))
            conn.commit()
            request.session['uid']=username
            response_dict={}
            status=1
            url='http://127.0.0.1:8000/polls/home/dashboard'
            response_dict.update({'status':status,'url1':url})
            return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
        else:
            status=2     ##uid already exists
            return HttpResponse(json.dumps(status),content_type='application/javascript')
    else:
        request.session['hack']='rohit'
        return render_to_response('polls/fbusername.htm',context_instance=RequestContext(request))

@never_cache
def login(request):
    if(request.method=="POST"):
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        print("cck"+uname)
        cursor.execute('''SELECT COUNT(*) FROM polls_userprofile where username=? AND password=?''',(uname,pwd,))
        conn.commit()
        c1=cursor.fetchone()
        ch1=c1[0]
        cursor.execute('''SELECT COUNT(*) FROM polls_userprofile where emailid=? AND password=?''',(uname,pwd,))
        conn.commit()
        c2=cursor.fetchone()
        ch2=c2[0]
        print("ckk"+str(ch1+ch2))
        if((ch1+ch2)!=0):
            if(ch2==1):
                cursor.execute('''SELECT username FROM polls_userprofile where emailid=? AND password=?''',(uname,pwd,))
                conn.commit()
                uname1=cursor.fetchone()
                request.session['uid']=uname1[0]
            else:
                request.session['uid']=uname
            response_dict={}
            response_dict.update({'flag':1})
            return HttpResponse(json.dumps(response_dict), content_type='application/javascript')
        else:
            response_dict={}
            response_dict.update({'flag':0})
            return HttpResponse(json.dumps(response_dict), content_type='application/javascript')

    else:
        return render_to_response('polls/findex.htm',{'request': request,'user': request.user,'username':"SignIn/SignUp"},context_instance=RequestContext(request))

@never_cache
def dashboard1(request):
    if(request.session.has_key('uid')):
        username=request.session['uid']
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        cursor.execute('''SELECT firstname,dob,contact,college,emailid FROM polls_userprofile where username=?''',(username,))
        conn.commit()
        cur=cursor.fetchall()
        firstname=cur[0][0]
        dob=cur[0][1]
        contact=cur[0][2]
        college=cur[0][3]
        ed=cur[0][4]
        cursor.execute('''SELECT picture FROM polls_profilepicture WHERE emailid=?''',(ed,))
        again=cursor.fetchone()
        cur_again=again[0][0]
        return render_to_response('polls/dashboard.html',{'username':username, 'name':firstname , 'dob':dob, 'contact':contact, 'college':college, 'image':cur_again},context_instance=RequestContext(request))
    else:
        return redirect("/polls/home/")

@never_cache
def selquiz(request):
    if(request.session.has_key('uid')):
        username=request.session['uid']
        utable=str(username)+"activity"
        print (utable)
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        cur="'"+str(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y"))+"'"
        cursor.execute('''SELECT quizname,date(endtime), time(endtime) FROM polls_quizglobal where (strftime('?', '''+cur+''') BETWEEN strftime('?', starttime) AND strftime('?', endtime))''')
        conn.commit()

        totalarr=cursor.fetchall()
        lim1=len(totalarr)

        print("njkjb"+str(lim1))
        quizname1=['']*lim1
        enddate=['']*lim1
        endtime=['']*lim1

        for i in range(0,lim1):
            quizname1[i]=totalarr[i][0]
            enddate[i]=totalarr[i][1]
            endtime[i]=totalarr[i][2]

        cursor.execute('''SELECT quizname,date(starttime), time(starttime) FROM polls_quizglobal where strftime('?', '''+cur+''') < strftime('?', starttime) ''')
        conn.commit()

        totalarr=cursor.fetchall()
        lim2=len(totalarr)
        print("totalarr="+str(totalarr))
        quizname2=['']*lim2
        startdate=['']*lim2
        print("here0")
        starttime=['']*lim2
        for i in range(0,lim2):
            quizname2[i]=totalarr[i][0]
            startdate[i]=totalarr[i][1]
            starttime[i]=totalarr[i][2]
        return render_to_response('polls/select_quiz.html',{'username':username, 'quiz1': quizname1,'quiz2':quizname2, 'dates1':endtime, 'dates2':startdate, 'times2':starttime, 'n1':lim1, 'n2':lim2},context_instance=RequestContext(request))

    else:
        return redirect("/polls/home/")

@never_cache
def quizgo(request,quizname):
    if(request.session.has_key('uid')):
        username=request.session['uid']
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        print("uname= "+str(username)+"knighter")
        #curtime = time.strftime("%H:%M:%S", time.gmtime())
        #curdate = time.strftime("%F", time.gmtime())
        #cur="'"+str(curdate)+"T"+str(curtime)+"'"
        cur="'"+str(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y"))+"'"
        cur1=(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y"))
        cur2=str(cur1).split()
        cur3=str(cur2[0])+"T"+str(cur2[1])
        utable=str(username)+"activity"
        cursor.execute('''SELECT COUNT(*) FROM '''+utable+''' where quizname =  ?''',(quizname,))
        conn.commit()
      #  print(cursor.fetchall[0][0])
        chk=cursor.fetchone()[0]
        print("chk="+str(chk))
        if(chk==0):
            print("here1")
            cursor.execute('''SELECT description,starttime,endtime,creator,marking,prizes,duration from polls_quizglobal where quizname=?''',(quizname,) )
            conn.commit()
            data1=cursor.fetchall()
            data=['']*7
            for i in range(0,7):
                data[i]=data1[0][i]
            desc=data[0]
            starttime=data[1]
            endtime=data[2]
            creator=data[3]
            marking=data[4]
            prizes=data[5]
            duration=data[6]
        #   desc=(cursor.fetchone())[0]
            flag=0   ##show register button in form
            return render_to_response('polls/quiz_first.htm',{"quizname":quizname,'duration':duration, "marking":marking, "prizes":prizes, "description":desc,"username":username, "creator":creator,"starttime":starttime,"endtime":endtime,"flag":flag},context_instance=RequestContext(request))

        cursor.execute('''SELECT status FROM '''+utable+''' where quizname =  ?''',(quizname,))
        conn.commit()
        chk=cursor.fetchone()[0]
        if(chk==1):
            print("here2")
            print("rgktuth")
            return render_to_response("polls/farzi.html",{'url':"/polls/events/selquiz/quiz/QuizPlay/Score/"+quizname+"/"},context_instance=RequestContext(request))

        cursor.execute('''SELECT COUNT(*) FROM polls_quizglobal where quizname =   ? and starttime > ?''',(quizname, cur,))
        conn.commit()
        chk=cursor.fetchone()[0]
        if(chk==0):
            print("here3")
            cursor.execute('''SELECT description,starttime,endtime,creator,marking,prizes,duration from polls_quizglobal where quizname=?''',(quizname,) )
            conn.commit()
            data1=cursor.fetchall()
            data=['']*7
            for i in range(0,7):
                data[i]=data1[0][i]
            desc=data[0]
            starttime=data[1]
            endtime=data[2]
            creator=data[3]
            marking=data[4]
            prizes=data[5]
            duration=data[6]
        #    desc=(cursor.fetchone())[0]
            flag=1       #don't show register button
            return render_to_response('polls/quiz_first.htm',{"quizname":quizname,'duration':duration, "marking":marking, "prizes":prizes, "username":username,"description":desc,"creator":creator,"starttime":starttime,"endtime":endtime,"flag":flag},context_instance=RequestContext(request))
        cursor.execute('''SELECT creator FROM polls_quizglobal where quizname= ? ''',(quizname,))
        conn.commit()
        chk=cursor.fetchone()[0]
        qtable="'"+quizname+str(chk)+"'"
        qltable="'"+quizname+str(chk)+"lboard'"
        cursor.execute('''SELECT ustarttime FROM '''+qltable+''' where username= ?''',(username,))
        conn.commit()
        ustarttime=cursor.fetchone()[0]
        if(ustarttime==None):
            print("here3")
            cursor.execute('''UPDATE '''+qltable+''' set ustarttime=? where username=?''',(cur3,username,))
            conn.commit()
        cursor.execute('''SELECT quesno,ques,opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10,image FROM '''+qtable+''' where qtype = ? ''',("Single Correct",))
        conn.commit()
        quizarrs=cursor.fetchall()
        nsques=len(quizarrs)
        cursor.execute('''SELECT quesno,ques,opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10,image FROM '''+qtable+''' where qtype = ? ''',("Multi Correct",))
        conn.commit()
        quizarrm=cursor.fetchall()
        nmques=len(quizarrm)
        cursor.execute('''select quesno,ques,image from '''+qtable+''' where qtype=?''',("input",))
        quizarrinput=cursor.fetchall()
        ninputques=len(quizarrinput)

        quizarrs1=[[]]
        for i in range(0,nsques):
            for j in range(0,13):
                if(quizarrs[i][j]!=""):
                    quizarrs1[i].append(quizarrs[i][j])
            if(i!=nsques-1):
                quizarrs1.append([])
        quizarrm1=[[]]
        for i in range(0,nmques):
            for j in range(0,13):
                if(quizarrm[i][j]!=""):
                    quizarrm1[i].append(quizarrm[i][j])
            if(i!=nmques-1):
                quizarrm1.append([])
        #quizarr1=[[""]*12]*nques
        #quizarr11=[[""]*12]*nques
        print(quizarrinput)
        print(ninputques)
        quizarrinput1=[[]]
        for i in range(0,ninputques):
            for j in range(0,3):
                if(quizarrinput[i][j]!=""):
                    quizarrinput1[i].append(quizarrinput[i][j])
            if(i!=ninputques-1):
                quizarrinput1.append([])
        cursor.execute('''SELECT  ansseq from '''+qltable+''' where username=? ''',(username,))
        conn.commit()
        nq=nsques+nmques+ninputques
        print(nq)
        ansseq=cursor.fetchone()[0]
        if (ansseq==None):
            ansseq="0000000000|"*nq
            print("none")
            cursor.execute('''Update '''+qltable+''' set ansseq=? where username=? ''',(ansseq,username))
            conn.commit()
        cursor.execute('''SELECT ustarttime from '''+qltable+''' where username=?''',(username,))
        conn.commit()
        ust=str(cursor.fetchone()[0])
        print(quizarrinput1)
        deltime=(cur1-datetime.datetime.strptime(ust, "%Y-%m-%dT%H:%M:%S")).seconds
        cursor.execute('''SELECT endtime,duration from polls_quizglobal where quizname=?''',(quizname,))
        conn.commit()
        tdata=cursor.fetchone()
        timme=(tdata[1]*60)-deltime
        qet=str(tdata[0])
        deltime2=(datetime.datetime.strptime(qet, "%Y-%m-%dT%H:%M:%S")-cur1).seconds
        if(timme>deltime2):
            timme=deltime2

            #quizarr[i][0]="a0"+str(quizarr[i][0])
        cursor.execute('''select mscc from polls_quizglobal where quizname=?''',(quizname,))
        scc=cursor.fetchone()[0]
        conn.commit()
        cursor.execute('''select msci from polls_quizglobal where quizname=?''',(quizname,))
        sci=cursor.fetchone()[0]
        conn.commit()
        cursor.execute('''select mmcc from polls_quizglobal where quizname=?''',(quizname,))
        mcc=cursor.fetchone()[0]
        conn.commit()
        cursor.execute('''select mmci from polls_quizglobal where quizname=?''',(quizname,))
        mci=cursor.fetchone()[0]
        conn.commit()
        cursor.execute('''select minputypecorrect from polls_quizglobal where quizname=?''',(quizname,))
        icc=cursor.fetchone()[0]
        conn.commit()
        cursor.execute('''select minputypeincorrect from polls_quizglobal where quizname=?''',(quizname,))
        ici=cursor.fetchone()[0]
        conn.commit()
        return render_to_response('polls/quiz.htm',{'username':username, 'tleft':timme, 'ansseq':ansseq,  'quizname':quizname, 'qds':quizarrs1, 'qdm':quizarrm1,'qdi':quizarrinput1 ,'nsques':nsques, 'nmques': nmques,'niques':ninputques,'scc':scc,'sci':sci,'mcc':mcc,'mci':mci,'icc':icc,'ici':ici},context_instance=RequestContext(request))

    else:
        return redirect("/polls/home/")

@never_cache
def RegCheck(request,quizname):
    if(request.session.has_key('uid')):
        uname=request.session.get('uid')
        print("uname="+str(uname))
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        cursor.execute('''SELECT COUNT(*) FROM '''+uname+'''activity where quizname=?''',(quizname,))
        conn.commit()
        cnt=(cursor.fetchone())[0]
        if(cnt==1):
            cursor.execute('''SELECT description,starttime,endtime,creator,marking,prizes,duration from polls_quizglobal where quizname=?''',(quizname,) )
            conn.commit()
            data1=cursor.fetchall()
            data=['']*7
            for i in range(0,7):
                data[i]=data1[0][i]
            desc=data[0]
            starttime=data[1]
            endtime=data[2]
            creator=data[3]
            marking=data[4]
            prizes=data[5]
            duration=data[6]
        #    desc=(cursor.fetchone())[0]
            flag=1       #don't show register button
            return render_to_response('polls/quiz_first.htm',{"quizname":quizname,'duration':duration, "marking":marking, "prizes":prizes, "username":uname,"description":desc,"creator":creator,"starttime":starttime,"endtime":endtime,"flag":flag},context_instance=RequestContext(request))
        else:   ##render the user quiz registration page,not made yet
            cursor.execute('''SELECT description,starttime,endtime,creator,marking,prizes,duration from polls_quizglobal where quizname=?''',(quizname,) )
            conn.commit()
            data1=cursor.fetchall()
            data=['']*7
            for i in range(0,7):
                data[i]=data1[0][i]
            desc=data[0]
            starttime=data[1]
            endtime=data[2]
            creator=data[3]
            marking=data[4]
            prizes=data[5]
            duration=data[6]
        #   desc=(cursor.fetchone())[0]
            flag=0   ##show register button in form
            return render_to_response('polls/quiz_first.htm',{"quizname":quizname,'duration':duration, "marking":marking, "prizes":prizes, "description":desc,"username":uname, "creator":creator,"starttime":starttime,"endtime":endtime,"flag":flag},context_instance=RequestContext(request))
    else:
        return redirect("/polls/home/")

@never_cache
def UserQuizReg(request,quizname):
    if(request.session.has_key('uid')):
        usernm=request.session.get('uid')
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        cursor.execute('''SELECT creator, starttime from polls_quizglobal where quizname=?''',(quizname,))
        conn.commit()
        tdata=cursor.fetchone()
        quizmaster=tdata[0]
        qstime=str(tdata[1])
        cursor.execute('''SELECT COUNT(*) FROM '''+quizname+quizmaster+'''lboard''' )
        conn.commit()
        serial=(cursor.fetchone())[0]
        serial=serial+1
        cursor.execute('''INSERT INTO '''+quizname+quizmaster+'''lboard (sno,username,points) values(?,?,?)''',(serial,usernm,0))
        conn.commit()
        cursor.execute('''INSERT INTO '''+usernm+'''activity (quizname,status,points) values(?,?,?)''',(quizname,0,0))
        conn.commit()
        cursor.execute('''SELECT emailid from polls_userprofile where username=?''',(usernm,))
        conn.commit()
        eid=(cursor.fetchone())[0]
        ####threading starts here
     #   Text='You have registered successfully for the quiz '+quizname
        #thread1 = myThread1(eid,quizname)
        #thread1.start()
        cur1=(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y"))
        qstime1=datetime.datetime.strptime(qstime, "%Y-%m-%dT%H:%M:%S")
        if(cur1<=qstime1):
            dict={"chk":1}
        else:
            dict={"chk":2}
        return HttpResponse(json.dumps(dict), content_type='application/javascript')
    else:
        return HttpResponse('you are not logged in.')

@never_cache
def QuizPlay(request,quizname):
    if(request.session.has_key('uid')):

        print("knight"+str(request.POST.get('ans')))
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        cursor.execute('''SELECT creator from polls_quizglobal where quizname=?''',(quizname,))
        conn.commit()
        quizmaster=(cursor.fetchone())[0]
        if(not request.session.has_key(quizname+'starttime')):
            print("check1")
            cursor.execute('''SELECT starttime,endtime,duration FROM polls_quizglobal where quizname=?''',(quizname,))
            conn.commit()
            data=cursor.fetchall()
            print(data[0][1])
            starttime=str(data[0][0])
            endtime=str(data[0][1])
            duration=int(data[0][2])
            duration=duration*1.0/1440
            print(quizname+quizmaster)
            cursor.execute('''select ustarttime from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
            conn.commit()
            ustarttime=str((cursor.fetchone())[0])
            if(datetime.datetime.strptime(ustarttime, "%Y-%m-%dT%H:%M:%S")+datetime.timedelta(duration)<=datetime.datetime.strptime(endtime, "%Y-%m-%dT%H:%M:%S")):
                    tmpuendtime=str(datetime.datetime.strptime(ustarttime, "%Y-%m-%dT%H:%M:%S")+datetime.timedelta(duration))
            else:
                    tmpuendtime=str(datetime.datetime.strptime(endtime, "%Y-%m-%dT%H:%M:%S"))
            print(tmpuendtime+" abc")
            if(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")> datetime.datetime.strptime(ustarttime, "%Y-%m-%dT%H:%M:%S") and datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")< datetime.datetime.strptime(tmpuendtime, "%Y-%m-%d %H:%M:%S")):
                    conn=sqlite3.connect('db.sqlite3')
                    cursor=conn.cursor()
                    cursor.execute('''Select creator from polls_quizglobal where quizname=?''',(quizname,))
                    creator=cursor.fetchone()[0]
                    cursor.execute('''Select status from '''+request.session.get('uid')+'''activity where quizname=?''',(quizname,))
                    status=cursor.fetchone()[0]
                    if(status==0):
                        answer=request.POST.get('ans')
              #         cursor.execute('''SELECT creator from polls_quizglobal where quizname=?''',(quizname))
               #        quizmaster=(cursor.fetchone())[0]
                        cursor.execute('''UPDATE '''+quizname+quizmaster+'''lboard set ansseq=? where username=?''',(answer,request.session.get('uid')))
                        conn.commit()
                        print('ertbqbqhj')
                        response_dict={}
                        response_dict.update({'response':''})
                        return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
                    else:
                        uname=request.session.get('uid')
                        conn=sqlite3.connect('db.sqlite3')
                        cursor=conn.cursor()
                        cursor.execute('''SELECT creator FROM polls_quizglobal where quizname=?''',(quizname,))
                        conn.commit()
                        quizmaster=(cursor.fetchone())[0]
                        cursor.execute('''SELECT ustarttime,uendtime from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
                        conn.commit()
                        data=cursor.fetchall()
                        ustarttime=str(data[0][0])
                        uendtime1=data[0][1]
                        print("btaaaa")
                        print(uendtime1)
                        print('chl')
                        if(uendtime1==None):
                            print('inside')
                            cursor.execute('''UPDATE '''+quizname+quizmaster+'''lboard set uendtime=? where username=?''',(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y"),request.session.get('uid')))
                      #  cursor.execute('''INSERT INTO '''+quizname+quizmaster+'''lboard set uendtime=? where username=?''',(uendtime,request.session.get('uid')))
                       # conn.commit()
                        print('outside')
                        cursor.execute('''SELECT uendtime from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
                        conn.commit()
                        uendtime=str(cursor.fetchone()[0])
                        uendtime2=datetime.datetime.strptime(uendtime,"%Y-%m-%d %H:%M:%S")
                        ustarttime2=datetime.datetime.strptime(ustarttime, "%Y-%m-%dT%H:%M:%S")
                        dur=uendtime2-ustarttime2
                        print("time")
                        print(dur)
                        cursor.execute('''Update '''+quizname+quizmaster+'''lboard set duration=? where username=?''',(dur.seconds,request.session.get('uid'))) #######check for format
                        conn.commit()
                        cursor.execute('''SELECT ansseq from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
                        conn.commit()
                        uansseq=(cursor.fetchone())[0]
                        str1=''
                        cursor.execute('''SELECT ans from '''+quizname+quizmaster+''' where qtype=?''',('Single Correct',))
                        conn.commit()
                        answer1=cursor.fetchall()
                        row=len(answer1)
                        for i in range(0,row):
                            str1=str1+answer1[i][0]+'|'
                        cursor.execute('''SELECT ans from '''+quizname+quizmaster+''' where qtype=?''',('Multi Correct',))
                        conn.commit()
                        answer1=cursor.fetchall()
                        row1=len(answer1)
                        for i in range(0,row1):
                            str1=str1+answer1[i][0]+'|'
                        cursor.execute('''SELECT ans from '''+quizname+quizmaster+''' where qtype=?''',('input',))
                        conn.commit()
                        answer1=cursor.fetchall()
                        row2=len(answer1)
                        for i in range(0,row2):
                            str1=str1+answer1[i][0]+'|'
                        s11=uansseq.split('|')
                        s22=str1.split('|')
                        cursor.execute('''SELECT mscc, msci,mmcc,mmci,minputypecorrect,minputypeincorrect from polls_quizglobal where quizname=?''',(quizname,))
                        conn.commit()
                        mscheme=cursor.fetchone()
                        score=0
                        attques=0
                        for i in range(0,row):
                            if(s11[i]==s22[i]):
                #                print("s11,s22,row="+str(s11)+str(s22)+str(row)+"  "+str(row1)+str(mscheme))
                                score+=mscheme[0]
                                attques+=1
                            elif(s11[i]!="0000000000"):
                                score-=abs(mscheme[1])
                                attques+=1
                        for i in range(row, row+row1):
                            if(s11[i]==s22[i]):
                                score+=mscheme[2]
                                attques+=1
                            elif(s11[i]!="0000000000"):
                                score-=abs(mscheme[3])
                                attques+=1
                        for i in range(row+row1,row+row1+row2):
                            if(s11[i]==s22[i]):
                                score+=mscheme[4]
                                attques+=1
                            elif(s11[i]!="0000000000" and s11[i]!=""):
                                score-=abs(mscheme[5])
                                attques+=1
                        maxmarks=row*mscheme[0]
                        maxmarks+=row1*mscheme[2]
                        maxmarks+=row2*mscheme[4]
                        totques=row+row1+row2
                        cursor.execute('''Update '''+quizname+quizmaster+'''lboard set points=? where username=?''',(score,request.session.get('uid')))
                        conn.commit()
                        cursor.execute('''select username,points,duration from '''+quizname+quizmaster+'''lboard order by points desc,duration''')      #####
                        conn.commit()
                        leaderdata1=cursor.fetchall()
                        print("ghjhk")
                        print(leaderdata1[0][0])
                        print(leaderdata1[0][1])
                        print(leaderdata1[0][2])
                        cursor.execute('''SELECT COUNT(*) FROM '''+quizname+quizmaster+'''lboard''')
                        conn.commit()
                        size1=(cursor.fetchone())[0]
                        usernm=['']*size1
                        points=['']*size1
                        duration=[0]*size1
                        j=0
                        for i in range(0,size1):
                            usernm[i]=leaderdata1[i][0]
                            points[i]=leaderdata1[i][1]
                            duration[i]=leaderdata1[i][2]
                            cursor.execute('''SELECT status from '''+usernm[i]+'''activity where quizname=?''',(quizname,))
                            if(cursor.fetchone()[0]):
                                j=j+1

                         ##   dura[i]=str(duration[i]//3600)+" : "+str((duration[i]%3600)//60)+" : "+str(((duration[i]%3600)%60))
                        usernm2=['']*j
                        points2=['']*j
                        duration2=[0]*j
                        dura2=['']*j
                        rank=0
                        k=0
                        for i in range(0,size1):
                            cursor.execute('''SELECT status from '''+usernm[i]+'''activity where quizname=?''',(quizname,))
                            if(cursor.fetchone()[0]):
                                print("cur;"+str(cursor.fetchone()[0]))
                                usernm2[k]=usernm[i]
                                print("usernm2:")
                                print(usernm2[j])
                                if(usernm2[k]==request.session.get('uid')):
                                    rank=k+1
                                points2[k]=points[i]
                                dura2[k]=str(duration[i]//3600)+" : "+str((duration[i]%3600)//60)+" : "+str(((duration[i]%3600)%60))
                                k=k+1

                        cursor.execute('''UPDATE '''+request.session.get('uid')+'''activity set status=?,points=?,starttime=?,endtime=? where quizname=?''',(1,score,ustarttime2,uendtime2,quizname))
                        conn.commit()
                      ##  twodarray=[usernm,points,duration]
                        return render_to_response("polls/quiz_table.htm",{'usernm':usernm2,'points':points2,'size':j,'duration':dura2,'username':uname, 'attques':attques,'totques':totques, 'dur':str(dur),'score':score,'maxmarks':maxmarks,'rank':rank},context_instance=RequestContext(request))
            else:
                    response_dict={}
                    response_dict.update({'response':'redirect'})
                    return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
        else:
            cursor.execute('''select ustarttime from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
            ustarttime=str((cursor.fetchone())[0])
            starttime=request.session.get(quizname+'starttime')
            endtime=request.session.get(quizname+'endtime')
            duration=request.session.get(quizname+'endtime')
            tmpuendtime=request.session.get(quizname+'tmpuendtime')
            print(tmpuendtime+" ad")
            print(ustarttime+"qui")
            if(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")> datetime.datetime.strptime(ustarttime, "%Y-%m-%dT%H:%M:%S") and datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")< datetime.datetime.strptime(tmpuendtime, "%Y-%m-%d %H:%M:%S")):
                conn=sqlite3.connect('db.sqlite3')
                cursor=conn.cursor()
                cursor.execute('''Select creator from polls_quizglobal where quizname=?''',(quizname,))
                creator=cursor.fetchone()[0]
                cursor.execute('''Select status from '''+request.session.get('uid')+'''activity where quizname=?''',(quizname,))
                status=cursor.fetchone()[0]
                if(status==0):
                    answer=request.POST.get('ans')
                    conn=sqlite3.connect('db.sqlite3')
                    cursor=conn.cursor()
                    cursor.execute('''UPDATE '''+quizname+quizmaster+'''lboard set ansseq=? where username=?''',(answer,request.session.get('uid')))
                    conn.commit()
                    print('fjhbqbqhj')
                    response_dict={}
                    response_dict.update({'response':''})
                    return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
                else:
                    uname=request.session.get('uid')
                    conn=sqlite3.connect('db.sqlite3')
                    cursor=conn.cursor()
                    cursor.execute('''SELECT creator FROM polls_quizglobal where quizname=?''',(quizname,))
                    conn.commit()
                    quizmaster=(cursor.fetchone())[0]
                    cursor.execute('''SELECT ustarttime,uendtime from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
                    conn.commit()
                    data=cursor.fetchall()
                    ustarttime=str(data[0][0])
                    uendtime1=data[0][1]
                    print("btaaaa")
                    print(uendtime1)
                    print('chl')
                    if(uendtime1==None):
                        print('inside')
                        cursor.execute('''UPDATE '''+quizname+quizmaster+'''lboard set uendtime=? where username=?''',(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y"),request.session.get('uid')))
                  #  cursor.execute('''INSERT INTO '''+quizname+quizmaster+'''lboard set uendtime=? where username=?''',(uendtime,request.session.get('uid')))
                   # conn.commit()
                    print('outside')
                    cursor.execute('''SELECT uendtime from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
                    conn.commit()
                    uendtime=str(cursor.fetchone()[0])
                    uendtime2=datetime.datetime.strptime(uendtime,"%Y-%m-%d %H:%M:%S")
                    ustarttime2=datetime.datetime.strptime(ustarttime, "%Y-%m-%dT%H:%M:%S")
                    dur=uendtime2-ustarttime2
                    print("time")
                    print(dur)
                    cursor.execute('''Update '''+quizname+quizmaster+'''lboard set duration=? where username=?''',(dur.seconds,request.session.get('uid'))) #######check for format
                    conn.commit()
                    cursor.execute('''SELECT ansseq from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
                    conn.commit()
                    uansseq=(cursor.fetchone())[0]
                    str1=''
                    cursor.execute('''SELECT ans from '''+quizname+quizmaster+''' where qtype=?''',('Single Correct',))
                    conn.commit()
                    answer1=cursor.fetchall()
                    row=len(answer1)
                    for i in range(0,row):
                        str1=str1+answer1[i][0]+'|'
                    cursor.execute('''SELECT ans from '''+quizname+quizmaster+''' where qtype=?''',('Multi Correct',))
                    conn.commit()
                    answer1=cursor.fetchall()
                    row1=len(answer1)
                    for i in range(0,row1):
                        str1=str1+answer1[i][0]+'|'
                    cursor.execute('''SELECT ans from '''+quizname+quizmaster+''' where qtype=?''',('input',))
                    conn.commit()
                    answer1=cursor.fetchall()
                    row2=len(answer1)
                    for i in range(0,row2):
                        str1=str1+answer1[i][0]+'|'
                    s11=uansseq.split('|')
                    s22=str1.split('|')
                    cursor.execute('''SELECT mscc, msci,mmcc,mmci,minputypecorrect,minputypeincorrect from polls_quizglobal where quizname=?''',(quizname,))
                    conn.commit()
                    mscheme=cursor.fetchone()
                    score=0
                    attques=0
                    for i in range(0,row):
                        if(s11[i]==s22[i]):
                            print("s11,s22,row="+str(s11)+str(s22)+str(row)+"  "+str(row1)+str(mscheme))
                            score+=mscheme[0]
                            attques+=1
                        elif(s11[i]!="0000000000"):
                            score-=abs(mscheme[1])
                            attques+=1
                    for i in range(row, row+row1):
                        if(s11[i]==s22[i]):
                            score+=mscheme[2]
                            attques+=1
                        elif(s11[i]!="0000000000"):
                            score-=abs(mscheme[3])
                            attques+=1
                    for i in range(row+row1,row+row1+row2):
                        if(s11[i]==s22[i]):
                            score+=mscheme[4]
                            attques+=1
                        elif(s11[i]!="0000000000" and s11[i]!=""):
                            score-=abs(mscheme[5])
                            attques+=1
                    maxmarks=row*mscheme[0]
                    maxmarks+=row1*mscheme[2]
                    maxmarks+=row2*mscheme[4]
                    totques=row+row1+row2
                    cursor.execute('''Update '''+quizname+quizmaster+'''lboard set points=? where username=?''',(score,request.session.get('uid')))
                    conn.commit()
                    cursor.execute('''select username,points,duration from '''+quizname+quizmaster+'''lboard order by points desc,duration''')      #####
                    conn.commit()
                    leaderdata1=cursor.fetchall()
                    print("ghjhk")
                    print(leaderdata1[0][0])
                    print(leaderdata1[0][1])
                    print(leaderdata1[0][2])
                    cursor.execute('''SELECT COUNT(*) FROM '''+quizname+quizmaster+'''lboard''')
                    conn.commit()
                    size1=(cursor.fetchone())[0]
                    usernm=['']*size1
                    points=['']*size1
                    duration=[0]*size1
                    j=0
                    for i in range(0,size1):
                        usernm[i]=leaderdata1[i][0]
                        points[i]=leaderdata1[i][1]
                        duration[i]=leaderdata1[i][2]
                        cursor.execute('''SELECT status from '''+usernm[i]+'''activity where quizname=?''',(quizname,))
                        if(cursor.fetchone()[0]):
                            j=j+1

                     ##   dura[i]=str(duration[i]//3600)+" : "+str((duration[i]%3600)//60)+" : "+str(((duration[i]%3600)%60))
                    usernm2=['']*j
                    points2=['']*j
                    duration2=[0]*j
                    dura2=['']*j
                    rank=0
                    k=0
                    for i in range(0,size1):
                        cursor.execute('''SELECT status from '''+usernm[i]+'''activity where quizname=?''',(quizname,))
                        if(cursor.fetchone()[0]):
                            print("cur;"+str(cursor.fetchone()[0]))
                            usernm2[k]=usernm[i]
                            print("usernm2:")
                            print(usernm2[j])
                            if(usernm2[k]==request.session.get('uid')):
                                rank=k+1
                            points2[k]=points[i]
                            dura2[k]=str(duration[i]//3600)+" : "+str((duration[i]%3600)//60)+" : "+str(((duration[i]%3600)%60))
                            k=k+1

                    cursor.execute('''UPDATE '''+request.session.get('uid')+'''activity set status=?,points=?,starttime=?,endtime=? where quizname=?''',(1,score,ustarttime2,uendtime2,quizname))
                    conn.commit()
                  ##  twodarray=[usernm,points,duration]
                    return render_to_response("polls/quiz_table.htm",{'usernm':usernm2,'points':points2,'size':j,'duration':dura2,'username':uname, 'attques':attques,'totques':totques, 'dur':str(dur),'score':score,'maxmarks':maxmarks,'rank':rank},context_instance=RequestContext(request))
            else:
                response_dict={}
                cursor.execute('''UPDATE '''+quizname+quizmaster+'''lboard set uendtime=? where username=?''',(request.session.get(quizname+'tmpuendtime'),request.session.get('uid')))
                conn.commit()
                response_dict.update({'response':'redirect'})
                return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
    else:
        return redirect("/polls/home/")

@never_cache
def func1(request):
  #conn=sqlite3.connect('db.sqlite3')
  #cursor=conn.cursor()
  #cursor.execute('''UPDATE polls_userprofile set interest1=? where emailid=?''',(intrchk(1),'vsandstorm0@gmail.com',))
  #conn.commit()
  return render_to_response('polls/quiz_first.htm',context_instance=RequestContext(request))

@never_cache
def QuizReg(request):
    quizregform=QuizRegForm()
    return render_to_response('polls/QuizReg.html',{'quizregform':quizregform},context_instance=RequestContext(request))

@never_cache
def Score(request,quizname):
    if(request.session.get('uid')):
            uname=request.session.get('uid')
            conn=sqlite3.connect('db.sqlite3')
            cursor=conn.cursor()
            cursor.execute('''SELECT creator FROM polls_quizglobal where quizname=?''',(quizname,))
            conn.commit()
            quizmaster=(cursor.fetchone())[0]
            cursor.execute('''SELECT ustarttime,uendtime from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
            conn.commit()
            data=cursor.fetchall()
            ustarttime=str(data[0][0])
            uendtime1=data[0][1]
            print("btaaaa")
            print(uendtime1)
            print('chl')
            if(uendtime1==None):
                print('inside')
                cursor.execute('''UPDATE '''+quizname+quizmaster+'''lboard set uendtime=? where username=?''',(datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y"),request.session.get('uid')))
          #  cursor.execute('''INSERT INTO '''+quizname+quizmaster+'''lboard set uendtime=? where username=?''',(uendtime,request.session.get('uid')))
           # conn.commit()
            print('outside')
            cursor.execute('''SELECT uendtime from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
            conn.commit()
            uendtime=str(cursor.fetchone()[0])
            uendtime2=datetime.datetime.strptime(uendtime,"%Y-%m-%d %H:%M:%S")
            ustarttime2=datetime.datetime.strptime(ustarttime, "%Y-%m-%dT%H:%M:%S")
            dur=uendtime2-ustarttime2
            print("time")
            print(dur)
            cursor.execute('''Update '''+quizname+quizmaster+'''lboard set duration=? where username=?''',(dur.seconds,request.session.get('uid'))) #######check for format
            conn.commit()
            cursor.execute('''SELECT ansseq from '''+quizname+quizmaster+'''lboard where username=?''',(request.session.get('uid'),))
            conn.commit()
            uansseq=(cursor.fetchone())[0]
            str1=''
            cursor.execute('''SELECT ans from '''+quizname+quizmaster+''' where qtype=?''',('Single Correct',))
            conn.commit()
            answer1=cursor.fetchall()
            row=len(answer1)
            for i in range(0,row):
                str1=str1+answer1[i][0]+'|'
            cursor.execute('''SELECT ans from '''+quizname+quizmaster+''' where qtype=?''',('Multi Correct',))
            conn.commit()
            answer1=cursor.fetchall()
            row1=len(answer1)
            for i in range(0,row1):
                str1=str1+answer1[i][0]+'|'
            cursor.execute('''SELECT ans from '''+quizname+quizmaster+''' where qtype=?''',('input',))
            conn.commit()
            answer1=cursor.fetchall()
            row2=len(answer1)
            for i in range(0,row2):
                str1=str1+answer1[i][0]+'|'
            s11=uansseq.split('|')
            s22=str1.split('|')
            cursor.execute('''SELECT mscc, msci,mmcc,mmci,minputypecorrect,minputypeincorrect from polls_quizglobal where quizname=?''',(quizname,))
            conn.commit()
            mscheme=cursor.fetchone()
            score=0
            attques=0
            for i in range(0,row):
                if(s11[i]==s22[i]):
                    print("s11,s22,row="+str(s11)+str(s22)+str(row)+"  "+str(row1)+str(mscheme))
                    score+=mscheme[0]
                    attques+=1
                elif(s11[i]!="0000000000"):
                    score-=abs(mscheme[1])
                    attques+=1
            for i in range(row, row+row1):
                if(s11[i]==s22[i]):
                    score+=mscheme[2]
                    attques+=1
                elif(s11[i]!="0000000000"):
                    score-=abs(mscheme[3])
                    attques+=1
            for i in range(row+row1,row+row1+row2):
                if(s11[i]==s22[i]):
                    score+=mscheme[4]
                    attques+=1
                elif(s11[i]!="0000000000" and s11[i]!=""):
                    score-=abs(mscheme[5])
                    attques+=1
            maxmarks=row*mscheme[0]
            maxmarks+=row1*mscheme[2]
            maxmarks+=row2*mscheme[4]
            totques=row+row1+row2
            cursor.execute('''Update '''+quizname+quizmaster+'''lboard set points=? where username=?''',(score,request.session.get('uid')))
            conn.commit()
            cursor.execute('''select username,points,duration from '''+quizname+quizmaster+'''lboard order by points desc,duration''')      #####
            conn.commit()
            leaderdata1=cursor.fetchall()
            print("ghjhk")
            print(leaderdata1[0][0])
            print(leaderdata1[0][1])
            print(leaderdata1[0][2])
            cursor.execute('''SELECT COUNT(*) FROM '''+quizname+quizmaster+'''lboard''')
            conn.commit()
            size1=(cursor.fetchone())[0]
            usernm=['']*size1
            points=['']*size1
            duration=[0]*size1
            j=0
            for i in range(0,size1):
                usernm[i]=leaderdata1[i][0]
                points[i]=leaderdata1[i][1]
                duration[i]=leaderdata1[i][2]
                cursor.execute('''SELECT status from '''+usernm[i]+'''activity where quizname=?''',(quizname,))
                if(cursor.fetchone()[0]):
                    j=j+1

             ##   dura[i]=str(duration[i]//3600)+" : "+str((duration[i]%3600)//60)+" : "+str(((duration[i]%3600)%60))
            usernm2=['']*j
            points2=['']*j
            duration2=[0]*j
            dura2=['']*j
            rank=0
            k=0
            for i in range(0,size1):
                cursor.execute('''SELECT status from '''+usernm[i]+'''activity where quizname=?''',(quizname,))
                if(cursor.fetchone()[0]):
           ##         print("cur;"+str(cursor.fetchone()[0]))
                    usernm2[k]=usernm[i]
                    print("usernm2:")
              #      print(usernm2[j])
                    if(usernm2[k]==request.session.get('uid')):
                        rank=k+1
                    points2[k]=points[i]
                    dura2[k]=str(duration[i]//3600)+" : "+str((duration[i]%3600)//60)+" : "+str(((duration[i]%3600)%60))
                    k=k+1

            cursor.execute('''UPDATE '''+request.session.get('uid')+'''activity set status=?,points=?,starttime=?,endtime=? where quizname=?''',(1,score,ustarttime2,uendtime2,quizname))
            conn.commit()
          ##  twodarray=[usernm,points,duration]
            return render_to_response("polls/quiz_table.htm",{'usernm':usernm2,'points':points2,'size':j,'duration':dura2,'username':uname, 'attques':attques,'totques':totques, 'dur':str(dur),'score':score,'maxmarks':maxmarks,'rank':rank},context_instance=RequestContext(request))
    else:
        return redirect("/polls/home/")


def EditOrCreate(request):
        loginid=request.POST['loginid']
        passwd=request.POST['passwd']
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        cursor.execute('''SELECT passwd from polls_quizreg where loginid=?''',(loginid,))
        passwd2=cursor.fetchone()
        passwd1=passwd2[0]
        print(passwd1)
        conn.commit()
        if(str(passwd1)==str(passwd)):
            request.session['quizmaster']=request.POST['loginid']
            cursor=conn.cursor()
            cursor.execute('''SELECT quizname from polls_quizglobal where creator=?''',(request.session['quizmaster'],))
            quiznamearray1=cursor.fetchall()
            conn.commit()
            cursor.execute('''SELECT COUNT (*) from polls_quizglobal where creator=?''',(request.session['quizmaster'],))
            asize=cursor.fetchone()
            quiznamearray=['']*asize[0]
            for i in range(0,asize[0]):
                quiznamearray[i]=quiznamearray1[i][0]
                print(quiznamearray[i]+" ")
            return render_to_response('polls/verma.htm',{'quiznamearray':quiznamearray,'asize':asize[0],'loginid':request.session['quizmaster']},context_instance=RequestContext(request))
        else:
            return HttpResponse("passwords don't match")


def test(request):

    return render_to_response('polls/quizm.htm',context_instance=RequestContext(request))


def CreateQuiz(request):
    conn=sqlite3.connect('db.sqlite3')
    cursor=conn.cursor()
    quizname=request.POST['quizname']
    starttime=request.POST['starttime']
    endtime=request.POST['endtime']
    duration=request.POST['duration']
    description=request.POST['desc']
    marking=request.POST['marking']
    prizes=request.POST['prizes']
    mscc=request.POST['mscc']
    msci=request.POST['msci']
    mmcc=request.POST['mmcc']
    mmci=request.POST['mmci']
    minputypecorrect=request.POST['mitc']
    minputypeincorrect=request.POST['miti']

    cursor.execute('''CREATE TABLE '''+quizname+request.session.get('quizmaster')+''' (
    quesno INTEGER PRIMARY KEY AUTOINCREMENT,
    ques TEXT NOT NULL,
    qtype TEXT NOT NULL,
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
    ans TEXT NOT NULL,
    image TEXT
    )''')
    conn.commit()
    cursor.execute('''CREATE TABLE '''+quizname+request.session.get('quizmaster')+'''lboard (
    sno INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    points INTEGER ,
    ustarttime TIME ,
    uendtime TIME ,
    duration TIME,
    ansseq TEXT

    )''')
    conn.commit()
    cursor.execute('''INSERT into polls_quizglobal (creator,quizname,starttime,endtime,duration,description,marking,prizes,mscc,msci,mmcc,mmci,minputypecorrect,minputypeincorrect) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(request.session.get('quizmaster'),quizname,starttime,endtime,duration,description,marking,prizes,mscc,msci,mmcc,mmci,minputypecorrect,minputypeincorrect))
    conn.commit()
    #cursor.execute('''SELECT time(endtime),time(starttime) from polls_quizglobal where quizname= ?''',(quiztablename,))
    #conn.commit()
    #wer=((cursor.fetchall()[0]))
    qarray=[]
    up=0
    return render_to_response("polls/quizm.htm",{'quizname':quizname ,'qarray': qarray, 'up':up},context_instance=RequestContext(request))


def quizuptab(request,quizname):
    if(request.method=='POST'):
        ques=request.POST['ques']
        options=request.POST['nq']
        qno=request.POST['qid']
        boo=request.POST['imgld']
        #if 'image' in request.FILES:
        if boo=="1":
            ph=request.FILES['imageabc']
            #ph=clean_content(ph0)
            import os
            from django.core.files.storage import default_storage
            from django.core.files.base import ContentFile
            from django.conf import settings
            path = default_storage.save('C:/Users/Akash/Desktop/Sarvasv_Git - Copy - Copy/static/temp.jpeg', ContentFile(ph.read()))
        qtype=request.POST['type']
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
        if(qtype!='input'):
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
        else:
            ans=str(opt1)
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        print("chala")
        quiztablename=quizname+request.session.get('quizmaster')
        if(qno=="0"):
            cursor.execute('''INSERT INTO '''+ quiztablename+''' (ques,qtype,options,opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10,ans) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(ques,qtype,options,opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10,ans))
            conn.commit()
        else:
            cursor.execute('''UPDATE'''+ quiztablename+''' SET ques=?, qtype=?, options=?, opt1=?, opt2=?, opt3=?, opt4=?, opt5=?, opt6=?, opt7=?, opt8=?, opt9=?, opt10=?, ans=? where quesno=?  ''',(ques,qtype,options,opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10,ans,qno))
            conn.commit()
        print(quiztablename+" "+quizname+" "+request.session.get('quizmaster'))
        cursor.execute('''Select ques from '''+ quiztablename)
        conn.commit()
        qarray=cursor.fetchall()
#Image code.
        if boo=="1":
            cursor.execute('''Select quesno from '''+quiztablename+''' where ques=?''',(ques,))
            conn.commit()
            sno=cursor.fetchone()[0]
            ret = save_file(path,quiztablename,sno)
            #print(ret)
            cursor.execute('''UPDATE '''+ quiztablename+''' SET image=? WHERE quesno=?''',(ret,sno))
#Image Code ends here.

        tabname=quiztablename
        cursor.execute(" Select Count (*) from "+tabname)
        conn.commit()
        up=cursor.fetchone()
        i=[0]*up[0]
        arrayq=[""]*(up[0])
        print(up[0])
        for k in range(0,up[0]):
            arrayq[k]=qarray[k][0]
            i[k]=k
        if(up[0]==0):
            arrayq=[]

        return render_to_response('polls/quizm.htm',{"qarray":arrayq,"quizname":quizname,"limits":i,"up":up[0]},context_instance=RequestContext(request))
        #return HttpResponse("Baad diya")


    else:
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        quiztablename=quizname+request.session.get('quizmaster')
        print(quiztablename+" "+quizname+" "+request.session.get('quizmaster'))
        cursor.execute('''Select ques from '''+ quiztablename )
        conn.commit()
        qarray=cursor.fetchall()
        tabname=quiztablename
        cursor.execute(" Select Count (*) from "+tabname)
        conn.commit()
        up=cursor.fetchone()
        i=[0]*up[0]
        arrayq=[""]*(up[0]+1)
        #print(up[0])
        for k in range(0,up[0]):
            arrayq[k]=qarray[k][0]
            i[k]=k
        if(up[0]==0):
            arrayq=[]
        #print(arrayq[1][0])
        return render_to_response('polls/quizm.htm',{"qarray":arrayq,"quizname":quizname,"limits":i,"up":up[0]},context_instance=RequestContext(request))
        #return render_to_response('polls/quizm.htm',context_instance=RequestContext(request))


def ChangeDate(request):
    quizname=str(request.POST.get('qn'))
    print("cool"+quizname)
    conn=sqlite3.connect('db.sqlite3')
    cursor=conn.cursor()
    cursor.execute('''SELECT * from polls_quizglobal where quizname=? ''',(quizname,))
    conn.commit()
    alpha=cursor.fetchone()
    response_dict={}
    print("asdfghjkl"+str(alpha[5]))
    response_dict.update({'quizname':alpha[2],'stime':alpha[3], 'etime':alpha[4], 'duration':alpha[5], 'desc':alpha[6], 'marking': alpha[7], 'prizes':alpha[8], 'mscc':alpha[9], 'msci':alpha[10], 'mmcc':alpha[11], 'mmci':alpha[12],'mitc':alpha[13],'miti':alpha[14]})
    return HttpResponse(json.dumps(response_dict),content_type='application/javascript')

    #trigger={1}     ##to trigger the alert box to remind that dates have been changed
    #return HttpResponse(trigger)
    #quiztablename=quizname+request.session.get('quizmaster')
    #print(quiztablename+" "+quizname+" "+request.session.get('quizmaster'))




def editq(request,quizname):
    if(request.method=="POST"):
        pry=request.POST.get("qid")
        pry1=pry[1:]
        pry2=int(pry1)+1
        print(pry2)
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        quiztablename=quizname+request.session.get('quizmaster')
        cursor.execute('''Select ques,qtype from '''+quiztablename+''' where quesno = ?''',(pry2,) )
        conn.commit()
        quesa=cursor.fetchall()
        ques=quesa[0]
        option=[""]*11
        cursor.execute('''Select opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8,opt9,opt10,qtype,image from '''+quiztablename+''' where quesno = ?''',(pry2,) )
        conn.commit()
        clap=cursor.fetchall()
        qtype=clap[0][10]
        print(clap[0][1])
        for i in range(1,11):
            option[i]=clap[0][i-1]
        cursor.execute('''Select options from '''+quiztablename+''' where quesno = ?''',(pry2,) )
        conn.commit()
        print(option)
        noptionsa=cursor.fetchone()
        noptions=noptionsa[0]
        if(qtype=='input'):
            noptions=1
            ans=option[1]
        else:
            cursor.execute('''Select ans from '''+quiztablename+''' where quesno = ?''',(pry2,) )
            conn.commit()
            ansa=cursor.fetchone()
            ans=ansa[0]
        print(ans)
        response_dict={}
    #response_dict.update({'ques':ques,'id':pry2, 'noptions':noptions, 'ans':ans,'opt1': option[1], 'opt2': option[2], 'opt3': option[3], 'opt4': option[4], 'opt5': option[5], 'opt6': option[6], 'opt7': option[7], 'opt8': option[8], 'opt9': option[9], 'opt10': option[10], })
        response_dict.update({'ques':ques,'id':pry2, 'type':qtype, 'noptions':noptions, 'ans':ans, 'option': option})
        return HttpResponse(json.dumps(response_dict),content_type='application/javascript')


def delq(request,quizname):
    if(request.method=="POST"):
        pry=request.POST.get("qid")
        pry1=pry[1:]
        pry2=int(pry1)+1
        print("yuio"+str(pry2))
        conn=sqlite3.connect('db.sqlite3')
        quiztablename=quizname+request.session.get('quizmaster')
        cursor=conn.cursor()
        cursor.execute('''DELETE FROM '''+quiztablename+''' WHERE quesno = ? ''',(pry2,))
        conn.commit()
        cursor.execute(" Select Count (*) from" + quiztablename )
        conn.commit()
        row=cursor.fetchone()
        for i in range(1,row[0]-pry2+3):
            cursor.execute('''UPDATE '''+quiztablename+''' SET quesno=? WHERE quesno = ?''',(pry2+i-1,pry2+i,))
            conn.commit()
        response_dict={}
        response_dict.update({'chk':1})
        request.method=""

        return HttpResponse(json.dumps(response_dict),content_type='application/javascript')


def delref(request,quizname):
    conn=sqlite3.connect('db.sqlite3')
    cursor=conn.cursor()
    quiztablename=quizname+request.session.get('quizmaster')
    print(quiztablename+" "+quizname+" "+request.session.get('quizmaster'))
    cursor.execute('''Select ques from '''+ quiztablename )
    conn.commit()
    qarray=cursor.fetchall()
    tabname=quiztablename
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
    return render_to_response('polls/quizm.htm',{"qarray":arrayq,"quizname":quizname,"limits":i,"up":up[0]},context_instance=RequestContext(request))


def editref(request,quizname):

    starttime=request.POST.get('starttime')
    endtime=request.POST.get('endtime')
    duration=request.POST.get('duration')
    description=request.POST.get('desc')
    marking=request.POST.get('marking')
    prizes=request.POST.get('prizes')
    mscc=request.POST.get('mscc')
    msci=request.POST.get('msci')
    mmcc=request.POST.get('mmcc')
    mmci=request.POST.get('mmci')
    minputypecorrect=request.POST.get('mitc')
    minputypeincorrect=request.POST.get('miti')
    conn=sqlite3.connect('db.sqlite3')
    cursor=conn.cursor()
    cursor.execute('''UPDATE polls_quizglobal set starttime=?, endtime=?, duration=?, description=?, marking=?, prizes=?, mscc=?, msci=?, mmcc=?, mmci=?,minputypecorrect=?,minputypeincorrect=? where quizname=?''',(starttime,endtime,duration,description,marking,prizes,mscc,msci,mmcc,mmci,minputypecorrect,minputypeincorrect,quizname))
    cursor=conn.cursor()
    quiztablename=quizname+request.session.get('quizmaster')
    print(quiztablename+" "+quizname+" "+request.session.get('quizmaster'))
    cursor.execute('''Select ques from '''+ quiztablename )
    conn.commit()
    qarray=cursor.fetchall()
    tabname=quiztablename
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
    return render_to_response('polls/quizm.htm',{"qarray":arrayq,"quizname":quizname,"limits":i,"up":up[0]},context_instance=RequestContext(request))

@never_cache
def dashboard(request):
    if(request.session.has_key('uid')):
        if(request.POST.get('value')=='editbutton'):                #########edit button in personalinfo pane
        #    username=request.POST.get('username')
                contact=request.POST.get('contact')
                dob=request.POST.get('dob')
            #    name=request.POST.get('name')

                response_dict={}

                conn=sqlite3.connect('db.sqlite3')
                cursor=conn.cursor()
                cursor.execute('''UPDATE polls_userprofile set contact=?,dob=? where username=?''',(contact,dob,request.session.get('uid')))
                gamma='success'
                response_dict.update({'gamma':gamma})
                return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
        elif(request.POST.get('value')=='pic'):
                pic=request.POST.get['picture']
                conn=sqlite3.connect('db.sqlite3')
                cursor=conn.cursor()
                cursor.execute('''SELECT emailid FROM polls_userprofile WHERE username=?''',(request.POST.get('uid'),))
                vare = cursor.fetchone()[0]
                cursor.execute('''SELECT COUNT(*) FROM polls_profilepicture where emailid=?''',(vare,))
                cntt2=cursor.fetchone()[0]
                if(cntt2==0):
                    new=ProfilePicture(emailid=vare, picture=pic)
                    new.save()
                else:
                    cursor.execute('''DELETE FROM polls_userprofile where emailid=?''',(vare,))
                    new=ProfilePicture(emailid=vare, picture=pic)
                    new.save()
                gamma='success'
                response_dict={}
                response_dict.update({'gamma':'success'})
                return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
        elif( request.POST.get('value')=='achievements'):
            conn=sqlite3.connect('db.sqlite3')
            cursor=conn.cursor()
            cursor.execute('''SELECT COUNT(*) from '''+request.session.get('uid')+'''activity where status=?''',(1,) )
            cnt=cursor.fetchone()[0]
            quizname=['']*cnt
            points=['']*cnt
            duration=['']*cnt
            endtime=['']*cnt
            cursor.execute('''select quizname from '''+request.session.get('uid')+'''activity where status=?''',(1,))
            quiz1=cursor.fetchall()
            j=0
            quiznm1=['']*cnt
            points1=['']*cnt
            rank1=['']*cnt
            dura1=['']*cnt
            for i in range(0,cnt):
                quizname[i]=quiz1[i][0]
                cursor.execute('''select points,duration from '''+quizname[i]+'''lboard where username=?''',(request.session.get('uid'),))
                points[i]=cursor.fetchall()[0][0]
                duration[i]=str(cursor.fetchall()[1][0])
                conn.commit()
                cursor.execute('''select endtime from polls_quizglobal where quizname=?''',(quizname[i],))
                endtime[i]=cursor.fetchone()[0]
                conn.commit()
                if(datetime.datetime.strptime(endtime, "%Y-%m-%dT%H:%M:%S")<=datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")):
                        quiznm1[j]=quizname[i]
                        points1[j]=points[i]
                        dura1[j]=duration[i]
                        cursor.execute('''select count(*) from '''+quizname[i]+'''lboard order by points desc,duration asc''')
                        cntr=cursor.fetchone()[0]
                        cursor.execute('''select username from '''+quizname[i]+'''lboard order by points desc,duration asc''')
                        user=cursor.fetchall()
                        for k in range(0,cntr):
                            if(user[k]==request.session.get('uid')):
                                rank1[j]=k+1
                                break
                        j=j+1
            response_dict={}
            response_dict.update({'quizzes':quiznm1,'points':points1,'ranks':rank1,'duration':dura1,'length':j})
            return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
        elif(request.POST.get('value')=='passwordchange'):
            origpasswd=request.POST.get('origpasswd')
            newpasswd=request.POST.get('newpasswd')
            conn=sqlite3.connect('db.sqlite3')
            cursor=conn.cursor()
            cursor.execute('''SELECT passwd from polls_userprofile where username=?''',(request.session.get('uid')))
            pass1=cursor.fetchone()[0]
            if(pass1==origpasswd):
                cursor.execute('''UPDATE polls_userprofile set password=? where username=?''',(newpasswd,request.session.get('uid')))
                gamma='okay'
                return HttpResponse(json.dumps(gamma),content_type='application/javascript')
            else:
                gamma='incorrect'
                return HttpResponse(json.dumps(gamma),content_type='application/javascript')
        elif(request.POST.get('value')=='curstatus'):
            conn=sqlite3.connect('db.sqlite3')
            cursor=conn.cursor()
            cursor.execute('''SELECT count(*) from '''+request.session.get('uid')+'''activity where status=?''',(1,))
            s1=cursor.fetchone()[0]
            cursor.execute('''select quizname from '''+request.session.get('uid')+'''activity where status=?''',(1,))
            conn.commit()
            quiz1=['']*s1
            points=['']*s1
            dur=['']*s1
            quiz2=['']*s1
            rank=['']*s1
            j=0
            quizn1=cursor.fetchall()
            for i in range(0,s1):
                quiz1[i]=quizn1[i][0]
                cursor.execute('''select endtime from polls_quizglobal where quizname=?''',(quiz1[i],))
                conn.commit()
                endtime=str(cursor.fetchone()[0])
                if(datetime.datetime.strptime(endtime, "%Y-%m-%dT%H:%M:%S")>=datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")):
                    quiz2[j]=quiz1[i]
                    cursor.execute('''select duration,points from '''+quiz2[j]+'''lboard where username=?''',(request.session.get('uid'),))
                    dur[j]=str(cursor.fetchall()[0][0])
                    points[j]=cursor.fetchall()[1][0]
                    cursor.execute('''select count(*) from '''+quiz2[j]+'''lboard order by points desc,duration asc''')
                    cntr=cursor.fetchone()[0]
                    cursor.execute('''select username from '''+quiz2[j]+'''lboard order by points desc,duration asc''')
                    user=cursor.fetchall()
                    for k in range(0,cntr):
                        if(user[k]==request.session.get('uid')):
                                rank[j]=k+1
                                break
                    j=j+1

            response_dict={}
            response_dict.update({'quizzes':quiz2,'points':points,'duration':dur,'ranks':rank,'len':j})
            return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
    ##    elif(request.POST.get('value')=='notifications'):
        elif(request.POST.get('value')=='userdetails'):
            username=request.session['uid']
            conn=sqlite3.connect('db.sqlite3')
            cursor=conn.cursor()
            cursor.execute('''SELECT firstname,dob,contact,college,emailid FROM polls_userprofile where username=?''',(username,))
            conn.commit()
            cur=cursor.fetchall()
            firstname=cur[0][0]
            dob=cur[0][1]
            contact=cur[0][2]
            college=cur[0][3]
            ed=cur[0][4]
            cursor.execute('''SELECT picture FROM polls_profilepicture WHERE emailid=?''',(ed,))
            again=cursor.fetchone()
            cur_again=again[0][0]
            response_dict={}
            response_dict.update({'name':firstname,'dob':dob,'contact':contact,'college':college,'image':cur_again})
            return HttpResponse(json.dumps(response_dict),content_type='application/javascript')
    else:
        return HttpResponse('you are not logged in')

#def read_file(filename):
#    with open(filename, 'rb') as f:
#        photo = f.read()
#    return photo

#def update_blob(quiztablename,quesno,filename):
#    data = read_file(filename)
#    query = "UPDTAE quiztablename " \
#            "SET photo = %s " \
#            "WHERE quesno = %s "

#    args = (data, quesno)
#    db_config = read_db_config()
#    try:
#        conn = MySQLConnection(**db_config)
#        cursor = conn.cursor()
#        cursor.execute(query, args)
#        conn.commit()
#    except Error as e:
#        print(e)
#    finally:
#        cursor.close()
#        conn.close()

#update_blob(144, "pictures\garth_stein.jpg")

#def write_file(data, filename):
#    with open(filename, 'wb') as f:
#        f.write(data)

#def read_blob(quiztablename,quesno, filename):
#    query = "SELECT photo FROM quiztablename WHERE quesno = %s"
#    db_config = read_db_config()

#    try:
#        # query blob data form the authors table
#        conn = MySQLConnection(**db_config)
#        cursor = conn.cursor()
#        cursor.execute(query, (quesno))
#        photo = cursor.fetchone()[0]

        # write blob data into a file
#        write_file(photo, filename)

#    except Error as e:
#        print(e)

#    finally:
#        cursor.close()
#        conn.close()

#read_blob(144,"output\garth_stein.jpg")
import os,sys
def save_file(path,quiztablename,quesno):
        dst1 = "C:/Users/Akash/Desktop/Sarvasv_Git - Copy - Copy/static/PH/"
        dst2 = quiztablename+str(quesno)+".jpg"
        dst = dst1+dst2
        conn=sqlite3.connect('db.sqlite3')
        cursor=conn.cursor()
        cursor.execute('''Select image from '''+quiztablename+''' where quesno = ?''',(quesno,))
        conn.commit()
        clap=cursor.fetchone()[0]
        print(clap)
        if clap is None:
            if path == "":
                dst = 0
                return dst
            else:
                os.link(path,dst)
                return dst
        else:
            if path == "":
                dst = 0
                return dst
            else:
                os.remove(dst)
                os.link(path,dst)
                return dst









