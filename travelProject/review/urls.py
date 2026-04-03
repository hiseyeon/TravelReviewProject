# review앱의 urls.py
from django.contrib import admin
from django.urls import path
from review import views

urlpatterns = [
    path("", views.review, name="review"),
]