from django.urls import path,include
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('insert',views.insert,name='insert'),
    path('teacherDelete/<tid>/',views.teacherDelete,name='delete' ),
    path('studentDelete/<stid>/',views.studentDelete,name='stdelete' ),
    path('courseDelete/<courseCode>/',views.courseDelete,name='ctdelete' ),
    path('studentlist/<courseCode>/<semesterID>/',views.studentList,name='studentlist' ),
    path('fileupload/',views.fileUpload,name='fileupload' ),
    path('reportgenerator/',views.reportGenerator,name='reportgenerator' ),
    path('gettakencourses/',views.gettakencourses,name='gettakencourses' ),
    path('getcourses/',views.getcourses,name='getcourses' ),
    path('getteacherid/',views.getteacherid,name='getteacherid' ),
]