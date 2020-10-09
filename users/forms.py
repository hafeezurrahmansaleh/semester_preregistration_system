from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import User
from student.models import StudentInfo
from teacher.models import TeacherInfo


class StudentSignUpForm(forms.ModelForm):
    mgs = ""
    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        cleaned_data = super(StudentSignUpForm, self).clean()
        raw_email = cleaned_data.get('email')
        stu = StudentInfo.objects.filter(stEmail__iexact=raw_email).first()
        usr = User.objects.filter(email__iexact=raw_email).first()
        print(raw_email)
        if usr is None:
            if stu is not None:
                # print(raw_email)
                user = super().save(commit=False)
                # username = form.cleaned_data.get('username')
                password = User.objects.make_random_password(length=6,
                                                             allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

                subject = 'Thank you for registering to our site'
                message = "you password is: " + password
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [raw_email, ]
                # send_mail(subject, message, email_from, recipient_list)

                user.username = stu.stID
                user.email = stu.stEmail
                user.set_password(password)
                user.is_student = True
                if commit:
                    user.save()
                    send_mail(subject, message, email_from, recipient_list)
                    StudentSignUpForm.mgs = "Successfully active you account. please check your Email!"
            else:
                #print("not found")
                # messages.error(self, 'not found.')
                StudentSignUpForm.mgs = "Your email not found. Please contact to Admin!"
                return redirect('student_signup')

        else:
            StudentSignUpForm.mgs = "Already have an account in this email!"
            # print("already have account in this email")
            return redirect('account_login')
        return user


#teacher
class TeacherSignUpForm(forms.ModelForm):
    mgs = ""
    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        cleaned_data = super(TeacherSignUpForm, self).clean()
        raw_email = cleaned_data.get('email')
        tec = TeacherInfo.objects.filter(tEmail__iexact=raw_email).first()
        usr = User.objects.filter(email__iexact=raw_email).first()
        if usr is None:
            if tec is not None:
                # print(raw_email)
                user = super().save(commit=False)
                # username = form.cleaned_data.get('username')
                password = User.objects.make_random_password(length=6, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

                subject = 'Thank you for registering to our site'
                message = "you password is: " + password
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [raw_email, ]
                #send_mail(subject, message, email_from, recipient_list)

                user.username = tec.tID
                user.email = tec.tEmail
                user.set_password(password)
                user.is_teacher = True
                if commit:
                    user.save()
                    send_mail(subject, message, email_from, recipient_list)
                    TeacherSignUpForm.mgs = "Successfully active you account. please check your Email!"
            else:
                # print("not found")
                # messages.error(self, 'not found.')
                TeacherSignUpForm.mgs = "Your email not found. Please contact to Admin!"
                return redirect('teacher_signup')
        else:
            # print("already have account in this email")
            TeacherSignUpForm.mgs = "Already have an account in this email!"
            return redirect('account_login')
        return user
