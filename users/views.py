from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
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
        elif request.user.is_admin:
            return redirect('index')
#         else:
#             return redirect('account_login')
    return redirect('account_login')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        mgs = StudentSignUpForm.mgs
        if 'Your email not' in mgs:
            messages.error(self.request, mgs)
        elif 'Already have' in mgs:
            messages.warning(self.request, mgs)
        elif 'Successfully active' in mgs:
            messages.success(self.request, mgs)
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
        mgs = TeacherSignUpForm.mgs
        if 'Your email not' in mgs:
            messages.error(self.request, mgs)
        elif 'Already have' in mgs:
            messages.warning(self.request, mgs)
        elif 'Successfully active' in mgs:
            messages.success(self.request, mgs)
        return redirect('account_login')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account_login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })