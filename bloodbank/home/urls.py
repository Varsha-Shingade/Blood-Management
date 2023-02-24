from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about', views.about,name='about'),
    path('login', views.login,name='login'),
    path('contact', views.contact,name='contact'),
    path('registration', views.registration,name='registration'),
    path('donar', views.donar,name='donar'),
    path('recipient', views.recipient,name='recipient'),
    path('alldonars', views.alldonars,name='alldonars'),
    path('allrecipients', views.allrecipients,name='allrecipients'),
    

]
