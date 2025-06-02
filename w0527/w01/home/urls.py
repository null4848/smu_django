from django.urls import path, include
from . import views

app_name = ''
urlpatterns = [
    path('', views.index, name='index'), # list url -> 함수 호출
]
