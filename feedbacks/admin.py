from django.contrib import admin
from feedbacks.models import Feedback


# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id', 'email', 'adviser_init', 'phone', 'issues']
    list_display_links = ['name', 'student_id', 'email']


admin.site.register(Feedback, FeedbackAdmin)
