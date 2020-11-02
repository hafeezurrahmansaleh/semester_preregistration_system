from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm

from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_student', 'is_teacher', 'is_admin',)}
         ),
    )
    list_display = ['email', 'username', 'first_name', 'last_name']


admin.site.register(User, UserAdmin)
