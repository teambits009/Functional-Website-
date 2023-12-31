"""OnlineschoolMgmt URL Configuration"""
"""The 'urlpatterns'list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.1/topics/http/urls\""""
"""Function Views"""
"""1. Add an import: from my_app import views  
         2. Add a URL to urlpatterns: path('', views.home, name = 'home')
Class-based views
        1. Add an import: from other_app.views import Home
        2. Add a URL to urlpatterns: path ('', Home.as_views(), name = 'home')
Including another URLconf
      1. Import the include() function: from django.urls import includes,
path
      2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))"""
 
from django.contrib import admin 
from django. urls import path 
#from app.views import *
from .views import loginPage,logoutPage,registerPage,home,addAttendance,addMarks,addNotice

urlpatterns = [

    path('',home ,name='home'),

    path('addAttendance/', addAttendance, name= 'addAttendance'),
    
    path('addMarks/', addMarks, name = 'addMarks'),

    path('addNotice/', addNotice, name = 'addNotice'),

    path('login/', loginPage,name = 'login'),
    path('logout/', logoutPage,name= 'logout'),
    path('register/', registerPage,name= 'register'),
    

]
