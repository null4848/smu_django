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

app_name ='board'

urlpatterns = [
    path('list/', views.list, name='list'),                 # 게시글 리스트
    path('view/<int:bno>/', views.view, name='view'),       # 게시글 보기
    path('write/', views.write, name='write'),              # 글쓰기
    path('update/<int:bno>', views.update, name='update'),  # 수정
    path('delete/<int:bno>', views.delete, name='delete'),  # 삭제
    path('reply/<int:bno>', views.reply, name='reply'),     # 답글 달기
]
