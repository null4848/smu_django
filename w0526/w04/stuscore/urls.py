from django.urls import path, include
from . import views

app_name='stuscore'
urlpatterns = [
    path('stuscore/', views.list, name='list'),
]