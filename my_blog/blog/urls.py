from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    path('', index),
    path("blogg.html", blog),
    path("contacts.html", contacts),
    path("about.html", about)
]
