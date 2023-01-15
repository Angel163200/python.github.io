from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name="about"),
    path('index', views.index, name="index"),
    path('blog', views.blog, name="blog"),
    path('blogdetails', views.blogdetails, name="blog-details"),
    path('roomdetails', views.roomdetails, name="room-details"),
    path('rooms', views.rooms, name="rooms"),
    path('login', views.login, name="login"),
    path('registration', views.registration, name="registration"),
    path('check', views.check, name="check"),
    path('check_username', views.check_username, name="check_username"),
    path('change_psw', views.change_psw, name="change_psw"),
    path('update_profile', views.update_profile, name="update_profile"),
    path('delete_account', views.delete_account, name="delete_account"),
    path('feedback', views.feedback, name="feedback"),
    path('select', views.select, name="select"),
    #path('destination/<int:n>', views.destination, name="destination" ),
    path('book_rooms', views.book_rooms, name="book_rooms"),
    path('payment', views.payment, name="payment"),
    path("logout", views.logout, name="logout"),
]