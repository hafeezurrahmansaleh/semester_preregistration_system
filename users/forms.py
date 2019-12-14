from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from student.models import StudentInfo
from teacher.models import TeacherInfo


class StudentSignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        cleaned_data = super(StudentSignUpForm, self).clean()
        raw_email = cleaned_data.get('email')
        stu = StudentInfo.objects.filter(stEmail=raw_email).first()
        if stu is not None:
            print(raw_email)
            user = super().save(commit=False)
            # username = form.cleaned_data.get('username')
            password = User.objects.make_random_password(length=6, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

            subject = 'Thank you for registering to our site'
            message = "you password is: " + password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [raw_email, ]
            send_mail(subject, message, email_from, recipient_list)

            user.username = stu.stID
            user.set_password(password)
            user.is_student = True
            if commit:
                user.save()
        else:
            print("not found")
        return user


#teacher
class TeacherSignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        cleaned_data = super(TeacherSignUpForm, self).clean()
        raw_email = cleaned_data.get('email')
        tec = TeacherInfo.objects.filter(tEmail=raw_email).first()
        if tec is not None:
            print(raw_email)
            user = super().save(commit=False)
            # username = form.cleaned_data.get('username')
            password = User.objects.make_random_password(length=6, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

            subject = 'Thank you for registering to our site'
            message = "you password is: " + password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [raw_email, ]
            send_mail(subject, message, email_from, recipient_list)

            user.username = tec.tID
            user.set_password(password)
            user.is_teacher = True
            if commit:
                user.save()
        else:
            print("not found")
        return user