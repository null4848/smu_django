"""
URL configuration for w01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = 'member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('join01/', views.join01, name='join01'), # 동의 페이지
    path('join02/', views.join02, name='join02'), # 회원가입 페이지
    path('join03/', views.join03, name='join03'), # 회원가입 페이지
    path('logout/', views.logout, name='logout'),
]
