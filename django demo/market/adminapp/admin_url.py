from django.urls import path
from . import views

urlpatterns = [
    path('admin', views.admin, name="admin"),
    path('view_customer', views.view_customer, name="view_customer"),
    path('view_seller', views.view_seller, name="view_seller"),
    path('delete_user/<int:id>', views.delete_user, name="delete_user"),
    path('accept_seller/<int:id>', views.accept_seller, name="accept_seller"),
    path('accept_seller1', views.accept_seller1, name="accept_seller1"),
    path('view_customer_feedback', views.view_customer_feedback, name="view_customer_feedback"),
    path('view_seller_feedback', views.view_seller_feedback, name="view_seller_feedback"),
]