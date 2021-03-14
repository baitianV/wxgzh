from django.contrib import admin
from django.urls import path,include
from . import views
#from .views.handle import Handle

from werobot.contrib.django import make_view



urlpatterns = [
    path('',views.index,name='index'),
    path('wx',views.handle_wx,name='wx'),
    path('robot',make_view(views.robot),name='robot'),
]

