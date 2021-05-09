from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages #import messages
from django.contrib.auth.models import User
from myapp.models import level1data,level2data, level3data,level4data,level5data,level6data ,answers,FinalScore,userInfo,clickedImages
from json import dumps , JSONDecodeError,JSONDecoder,JSONEncoder
import json
from django.db.models.query_utils import DeferredAttribute
from django.views.decorators.cache import cache_control


# Create your views here.

def leaderboard(request):
    f= FinalScore.objects.all().order_by('-Fscore')
    num=len(f)
    params={'Score':f,'num':num}
    return render(request ,'leaderboard.html',params,)


def  index(request):
    return render(request ,'index.html')


def ind(request):
    print(request.user)
    u = userInfo.objects.filter(name=request.user).first()
    if u is not None:
        params={'Clevel':u.Clevel}
        return render(request ,'index.html',params)
    else:
        return render(request,"index.html")


def ending(request):
    return render(request,"end.html")

# levels
@cache_control(no_cache=True,must_revalidate=True)
def level1(request,default='default'):

    print(default)
    imag = level1data.objects.only("img_id","img_src")
    num=len(imag)
    print(request.user)
    f= FinalScore.objects.get(name = request.user)
    u = userInfo.objects.get(name=request.user)
    # print(User.username)
    print(request.path)
    params = { 'level1imag':imag ,
    'range':range(num),'cnt':u.level1ClickCount,'userScore':f.Fscore,'Clevel':u.Clevel

    }
    # level1.refresh_from_db()

    u.currentLevel=1
    c= u.Clevel
    u.save()
    if u.Clevel=="level1" or u.level1=="false":
        return render(request,"level1.html",params)
    elif(u.level1=="true"):
        return redirect(c)

@cache_control(no_cache=True,must_revalidate=True)
def level2(request,default='default'):
    print(default)
    imag = level2data.objects.only("img_id","img_src")
    num=len(imag)
    print(request.user)
    f= FinalScore.objects.get(name = request.user)
    u = userInfo.objects.get(name=request.user)
    u.level1="true"
    # print(User.username)

    if u.currentLevel==1:
        u.currentLevel=2
        u.Clevel="level2"
        u.save()

    print(request.path)

    params = { 'level2imag':imag ,
    'range':range(num),'cnt':u.level2ClickCount,'userScore':f.Fscore,'Clevel':u.Clevel

    }
    u.refresh_from_db()
    c= u.Clevel
    u.save()
    if u.Clevel=="level2" or u.level2=="false":
        return render(request,"level2.html",params)
    elif( u.level2=="true"):
        return redirect(c)

@cache_control(no_cache=True,must_revalidate=True)
def level3(request,default='default'):
    print(default)
    imag = level3data.objects.only("img_id","img_src")
    num=len(imag)
    print(request.user)
    f= FinalScore.objects.get(name = request.user)
    u = userInfo.objects.get(name=request.user)
    u.level2="true"
    # print(User.username)

    if u.currentLevel==2:
        u.currentLevel=3
        u.Clevel="level3"
        u.save()

    print(request.path)

    params = { 'level3imag':imag ,
    'range':range(num),'cnt':u.level3ClickCount,'userScore':f.Fscore,'Clevel':u.Clevel

    }
    u.refresh_from_db()
    c= u.Clevel
    u.save()
    if u.Clevel=="level3" or u.level3=="false":
        return render(request,"level3.html",params)
    elif( u.level3=="true"):
        return redirect(c)

@cache_control(no_cache=True,must_revalidate=True)
def level4(request,default='default'):
    print(default)
    imag = level4data.objects.only("img_id","img_src")
    num=len(imag)
    print(request.user)
    f= FinalScore.objects.get(name = request.user)
    u = userInfo.objects.get(name=request.user)
    u.level3="true"
    # print(User.username)

    if u.currentLevel==3:
        u.currentLevel=4
        u.Clevel="level4"
        u.save()

    print(request.path)

    params = { 'level4imag':imag ,
    'range':range(num),'cnt':u.level4ClickCount,'userScore':f.Fscore,'Clevel':u.Clevel

    }
    u.refresh_from_db()
    c= u.Clevel
    u.save()
    if u.Clevel=="level4" or u.level4=="false":
        return render(request,"level4.html",params)
    elif( u.level4=="true"):
        return redirect(c)


# login
def loginuser(request):
    if request.method =="POST":
        lusername = request.POST['loginusername']
        lpass = request.POST['loginpass']
        user = authenticate(username = lusername,password = lpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            # AllLogin.objects.create(lusername)
            return redirect('index.html')

        else:
            messages.error(request,'Inavlid Credentials ,Please try again')
            return redirect('index.html')
    else:
        return HttpResponse('404-Not Found')

#logout 
def logoutuser(request):
    imag = level1data.objects.all()
    for i in imag:
        i.img_flag = "false"
        i.save()


    u = userInfo.objects.get(name=request.user)
    f = FinalScore.objects.get(name=request.user)
    if(f.Fscore<u.score):
        f.Fscore=u.score
        f.save()

    p = userInfo.objects.all()

    for i in p:
        i = i.__class__._default_manager.get(pk=i.pk)

    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect('index.html')

# Register
def register(request):
    if request.method =="POST":
        #  post parameters
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous inputs
        #username must be of 10 characters
        if len(username)>10:
            messages.error(request,"User name must be less than 10 characters")
            return redirect('index.html')

        #username should be alphanumeric
        if not username.isalnum():
            messages.error(request,"User name must be alphanumeric")
            return redirect('index.html')

        # passwords should match
        if pass1 != pass2:
            messages.error(request,"passwords donot match")
            return redirect('index.html')


        # create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        f = FinalScore(name=username)
        f.save()
        # c = clickCount(name=username)
        # c.save()
        u = userInfo(name=username)
        u.save()
        messages.success(request," your account has been successfully created")
        return redirect('index.html')
    else:
        return HttpResponse('404-Not Found')


# ClickFunctionalityOfLevels
def click(request):
    print(request.user)
    print(request.body)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    img_Id = body['id']
    img = level1data.objects.filter(img_id=img_Id).first()
    img_data = ""
    f= FinalScore.objects.get(name = request.user)
    u =userInfo.objects.get(name=request.user)
    cnt = u.level1ClickCount

    if(img_Id!="default"):
        p = clickedImages.objects.filter(name=request.user , imgId=img_Id).first()
        print(p)
        if(p==None and cnt>0):
            p=clickedImages(name=request.user,imgId = img_Id)
            p.save()
            cnt = cnt-1
            if(cnt>0):
                u.level1ClickCount = cnt
                img_data=img.img_data
            elif cnt==0:
                u.level1ClickCount=0
                img_data=img.img_data
                u.save()
        elif(p!=None):
             img_data=img.img_data


    user = User.objects.all()

    # print(user)
    print(request.user)
    u.save()
    u.refresh_from_db()
    context={'cnt':u.level1ClickCount,"userScore":f.Fscore,"img_data":img_data}

    # return HttpResponse({cnt:c.count})
    return HttpResponse(json.dumps(context))

def click2(request):
    print(request.user)
    print(request.body)
    f= FinalScore.objects.get(name = request.user)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    img_Id = body['id']
    img = level2data.objects.filter(img_id=img_Id).first()
    img_data = ""
    u =userInfo.objects.get(name=request.user)
    cnt = u.level2ClickCount
    if(img_Id!="default"):
        p = clickedImages.objects.filter(name=request.user , imgId=img_Id).first()
        print(p)
        if(p==None and cnt>0):
            p=clickedImages(name=request.user,imgId = img_Id)
            p.save()
            cnt = cnt-1
            if(cnt>0):
                img_data=img.img_data
                u.level2ClickCount = cnt
                img_data=img.img_data
            elif cnt==0:
                u.level2ClickCount=0
                u.save()
        elif(p!=None):
             img_data=img.img_data


    user = User.objects.all()

    # print(user)
    print(request.user)
    u.save()
    u.refresh_from_db()
    context={'cnt':u.level2ClickCount,"userScore":f.Fscore,"img_data":img_data}

    # return HttpResponse({cnt:c.count})
    return HttpResponse(json.dumps(context))

def click3(request):
    print(request.user)
    print(request.body)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    img_Id = body['id']
    img=level3data.objects.filter(img_id=img_Id).first()
    img_data=""
    f= FinalScore.objects.get(name = request.user)
    u =userInfo.objects.get(name=request.user)
    cnt = u.level3ClickCount
    if(img_Id!="default"):
        p = clickedImages.objects.filter(name=request.user , imgId=img_Id).first()
        print(p)        
        if(p==None and cnt>0):
            p=clickedImages(name=request.user,imgId = img_Id)
            p.save()
            cnt = cnt-1
            if(cnt>0):
                u.level3ClickCount = cnt
                img_data=img.img_data
            elif cnt==0:
                img_data=img.img_data
                u.level3ClickCount=0
                u.save()
        elif(p!=None):
             img_data=img.img_data
    user = User.objects.all()
    # print(user)
    print(request.user)
    u.save()
    u.refresh_from_db()
    print(img.img_data)
    context={'cnt':u.level3ClickCount,"userScore":f.Fscore,"img_data":img_data}
    # return HttpResponse({cnt:c.count})
    return HttpResponse(json.dumps(context))

def click4(request):
    print(request.user)
    print(request.body)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    img_Id = body['id']
    img = level4data.objects.filter(img_id=img_Id).first()
    img_data=""
    f= FinalScore.objects.get(name = request.user)
    u =userInfo.objects.get(name=request.user)
    cnt = u.level4ClickCount
    if(img_Id!="default"):
        p = clickedImages.objects.filter(name=request.user , imgId=img_Id).first()
        print(p)
        if(p==None and cnt>0):
            p=clickedImages(name=request.user,imgId = img_Id)
            p.save()
            cnt = cnt-1
            if(cnt>0):
                u.level4ClickCount = cnt
                img_data=img.img_data
            elif cnt==0:
                img_data=img.img_data
                u.level4ClickCount=0
                u.save()
        elif(p!=None):
             img_data=img.img_data

    user = User.objects.all()
    # print(user)
    print(request.user)
    u.save()
    u.refresh_from_db()
    context={'cnt':u.level4ClickCount,"userScore":f.Fscore,"img_data":img_data}
    # return HttpResponse({cnt:c.count})
    return HttpResponse(json.dumps(context))


# answerCheck
def answerCheck(request):
    flag=False
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    u =userInfo.objects.get(name=request.user)
    f= FinalScore.objects.get(name = request.user)
    print(request.body)
    lname= body['level']
    Panswer = body['ans']
    # dict = {'level1':u.level1score,'level2':u.level2score,'level3':u.level3score}
    ans = answers.objects.get(levels=lname)
    if(Panswer ==ans.answer):
        flag = True
        ft = False
        if(lname=='level1'and u.level1score=="false"):
            ft=True
            u.level1score="true"
        elif(lname=='level2'and u.level2score=="false"):
            ft=True
            u.level2score="true"
        elif(lname=='level3'and u.level3score=="false"):
            ft=True
            u.level3score="true"
        elif(lname=='level4'and u.level4score=="false"):
            ft=True
            u.level4score="true"

        if(ft==True):
            u.score+=10
            f.Fscore=u.score

    u.save()
    f.save()
    context={'flag':flag,"userScore":f.Fscore}

    return HttpResponse(json.dumps(context))

 






