from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    path('student/signup/', user_views.StudentSignUpView.as_view(), name='student_signup'),
    path('teacher/signup/', user_views.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('', include('allauth.urls')),
    path('profile/', user_views.home, name='profile'),
    path('user_logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]
