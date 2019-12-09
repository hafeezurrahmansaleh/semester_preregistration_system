from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.studentPanelHome,name='stphome'),
    path('findcourse',views.findCourse,name='findcourse')
]