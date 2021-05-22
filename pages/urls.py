
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('questions', views.list_data, name='questions'),
    path('search', views.search, name='search'),
]
