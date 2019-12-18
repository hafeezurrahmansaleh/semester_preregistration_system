from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import teacher_required
from .models import *

def teacherPanelHome(request):
    return render(request, 'teacherpanel/tphome.html')