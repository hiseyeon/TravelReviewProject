from django.contrib import admin
from django.urls import path
from reviewHome import views

urlpatterns = [
    path("", views.reviewHome, name="reviewHome"),
    path("blog_list/", views.blog_list, name="blog_list"),
    path("blog_detail/<int:blog_id>/", views.blog_detail, name="blog_detail"),
    path("blog_update/<int:id>/", views.blog_update, name="blog_update"),
    path("blog_delete/<int:id>/", views.blog_delete, name="blog_delete"),
]