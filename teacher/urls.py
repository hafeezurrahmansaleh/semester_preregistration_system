from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.teacherPanelHome,name='tphome'),
    path('advisestudent/<stID>',views.advisestudent,name='advisestudent'),
    path('registeredCourses',views.registeredCourses,name='registeredCourses'),
    path('saveremark',views.saveRemark,name='saveremark'),
    path('updateregistration/<sem>/<sid>',views.updateRegistration,name='updateregistration'),
    path('savecourse/',views.saveCourse,name='savecourse'),
    path('findcourse/',views.findCourse,name='findcourse'),
    path('dropcourse/',views.dropCourse,name='dropcourse'),
    path('finalregistration/<semid>/<tinitial>',views.finalregistration,name='finalregistration'),
    path('findregstatus/',views.findregstatus,name='findregstatus'),
    path('changeregstatus/',views.changeregstatus,name='changeregstatus'),
    path('findpaymentstatus/',views.findpaymentstatus,name='findpaymentstatus'),
]