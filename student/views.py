import jsonify as jsonify
from django.core import serializers
from django.core.serializers import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from adminpanel.models import Courses

def studentPanelHome(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'studentpanel/stphome.html',context)
@csrf_exempt
def findCourse(request):
    term = request.POST['term']
    semester = request.POST['semester']
    level = request.POST['level']
    courses = Courses.objects.filter(level=level, term=term)
    # print(level+semester)
    data = serializers.serialize('json', courses)
    return HttpResponse(data)