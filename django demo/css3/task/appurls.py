from django.urls import path
from . import views

urlpatterns = [
    path('seat', views.seat, name="seat"),
    path('index', views.index, name="index"),
    path('genre', views.genre, name="genre"),
    path('about', views.about, name="about"),
    path('single', views.single, name="single"),
]