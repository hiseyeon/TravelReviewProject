from django.contrib import admin
from django.urls import path
from country import views

urlpatterns = [
    path("", views.country, name="country"),
]