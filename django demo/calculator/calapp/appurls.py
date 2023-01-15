from django.urls import path, re_path
from . import views
urlpatterns = [

    path('add/<int:num1>/<int:num2>', views.add),
    path('diff/<int:num1>/<int:num2>', views.diff),
    path('pro/<int:num1>/<int:num2>', views.pro),
    path('quo/<int:num1>/<int:num2>', views.quo),
    path('calculate/<int:num1>', views.calculate)
    ]