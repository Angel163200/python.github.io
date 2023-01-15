from django.urls import path
from . import views
urlpatterns = [


    path('deleteuser/<int:id>',views.deleteuser,name='deleteuser')

]