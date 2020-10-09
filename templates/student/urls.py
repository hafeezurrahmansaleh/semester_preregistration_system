from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.studentPanelHome,name='stphome'),
    path('findcourse',views.findCourse,name='findcourse'),
    path('registercourse',views.registerCourse,name='registercourse'),
    path('findregisteredcourses',views.findRegisteredCourses,name='findregisteredcourses'),
    path('dropcourses',views.dropCourses,name='dropcourses'),
    path('getstudentpersection',views.getstudentpersection,name='getstudentpersection'),
]