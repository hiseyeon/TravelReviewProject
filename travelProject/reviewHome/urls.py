from django.contrib import admin
from django.urls import path
from reviewHome import views

urlpatterns = [
    path("", views.reviewHome, name="reviewHome"),
]