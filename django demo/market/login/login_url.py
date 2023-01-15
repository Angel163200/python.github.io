from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('feedback', views.feedback, name="feedback"),
    path('delete_account', views.delete_account, name="delete_account"),
    path('change_psw', views.change_psw, name="change_psw"),
    path('checkusername/',views.checkusername,name='checkusername'),
    path('checkph/',views.checkph,name='checkph'),
]