from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about/<int:social_media_id>', about , name = "about"),
    path('service/<int:customer_id>', service , name = "service"),
    path('team/<int:teammember_id>', team , name = "team"),
    path('why/', why )
    
]