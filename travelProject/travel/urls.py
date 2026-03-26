from django.contrib import admin
from django.urls import path
from travel import views

urlpatterns = [
    path("", views.home, name="home"), # 첫번째 path
    path("create/", views.home, name="home"), # 두번째 path
]