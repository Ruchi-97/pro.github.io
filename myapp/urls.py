
from django.contrib import admin
from django.urls import path ,include 
from django.conf.urls import handler400
from django.conf.urls import url
from myapp import views
from django.contrib import messages


urlpatterns = [
  path("",views.index, name='index'),
  path('register',views.register,name='register'),
  path("index.html",views.ind,name="ind"),
  path('login',views.loginuser,name='login'),
  path('logout',views.logoutuser,name='logout'), 

  path("level1.html",views.level1, name='level1'),
  path("level2.html",views.level2, name='level2'),
  path("level3.html",views.level3, name='level3'),
  path("level4.html",views.level4, name='level4'),
  path('end.html',views.ending,name='end'), 

  path("leaderboard.html",views.leaderboard, name='leaderboard'),
  
  path('click',views.click,name='click'),
  path('click2',views.click2,name='click2'),
  path('click3',views.click3,name='click3'),
  path('click4',views.click4,name='click4'),
  path('answerCheck',views.answerCheck,name='answerCheck'),
 

]
