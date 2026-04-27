"""
URL configuration for travelProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from travel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", views.home, name="home"), #127.0.0.1:8000/
    path("home/", include("travel.urls")), # 127.0.0.1:8000/home/ 이 blog앱의 기본 Path로 설정됨
    path("country/", include("country.urls")),
    path("review/", include("review.urls")),
    path("reviewHome/", include("reviewHome.urls")),


    path('create/', views.create, name='create'),
    path('accounts/',include('accounts.urls', namespace='accounts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
