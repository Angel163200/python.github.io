from django.urls import path
from . import views

urlpatterns = [

    path('message', views.message),
    path('message/<str:name>', views.message1),
    path('index/', views.index, name='index'),
]
