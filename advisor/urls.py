from django.urls import path,include
from . import views
urlpatterns = [
    path('advisorhome/',views.advisorHome,name='advisorhome')
]