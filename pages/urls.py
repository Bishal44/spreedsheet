"""
spreedsheet
Created by Bishal on 14 May 2021
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
