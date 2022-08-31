from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('sturecords/', views.StudentAPI.as_view()),
]