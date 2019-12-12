from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('index',views.index,name='index'),
    path('insert',views.insert,name='insert'),
]