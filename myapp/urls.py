from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('about/',about),
    path('service/',service),
    path('team/',team),
    path('why/',why)
    
]