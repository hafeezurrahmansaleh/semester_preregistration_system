from django.shortcuts import render

from .models import *

def teacherPanelHome(request):
    return render(request, 'teacherpanel/tphome.html')