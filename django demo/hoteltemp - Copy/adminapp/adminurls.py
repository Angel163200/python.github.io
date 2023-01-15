from django.urls import path
from . import views

urlpatterns = [
    path('admin', views.admin, name="admin"),
    path('admins', views.admins, name="admins"),
    path('view_users', views.view_users, name="view_users"),
    path('view_feedbacks', views.view_feedbacks, name="view_feedbacks"),
    path('delete_user/<int:id>', views.delete_user, name="delete_user"),
    path('view_rooms', views.view_rooms, name="view_rooms"),
    path('edit_rooms/<int:id>', views.edit_rooms, name="edit_rooms"),
    path('add_rooms', views.add_rooms, name="add_rooms"),
    path('delete_rooms/<int:id>', views.delete_rooms, name="delete_rooms"),
    path('view_booked_rooms', views.view_booked_rooms, name="view_booked_rooms"),
    ]
