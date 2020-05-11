from django.contrib import admin
from .models import *


admin.site.register(Courses)
admin.site.register(CoursePreRegistration)
admin.site.register(SemesterInfo)
admin.site.register(CourseSection)
admin.site.register(Remarks)
admin.site.register(WaiverInfo)
admin.site.register(PaymentInfo)
