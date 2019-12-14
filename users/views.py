from django.shortcuts import render, redirect
# decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from .forms import UserRegisterForm
from django.views.generic import CreateView, TemplateView
from .forms import StudentSignUpForm, TeacherSignUpForm
from .models import User


# class SignUpView(TemplateView):
#     template_name = 'landing/signup.html'
#
#
def home(request):
    if request.user.is_authenticated:
        if request.user.is_student:
            return redirect('stphome')
        elif request.user.is_teacher:
            return redirect('tphome')
#         else:
#             return redirect('account_login')
    # return redirect('account_login')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        # login(self.request, user)
        return redirect('account_login')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        # login(self.request, user)
        return redirect('account_login')