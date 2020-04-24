from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.teacherPanelHome,name='tphome'),
    path('advisestudent/<stID>',views.advisestudent,name='advisestudent'),
]