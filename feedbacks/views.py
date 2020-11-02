from django.shortcuts import render
from feedbacks.models import Feedback
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import get_user_model

User = get_user_model()


def feedback(request):
    status = Feedback.objects.all()
    mail_qs = User.objects.filter(is_admin=True).values_list('email', flat=True)
    get_mail = list(mail_qs)

    if request.method == 'POST':
        name = request.POST["name"]
        student_id = request.POST["student_id"]
        adviser_init = request.POST["adviser_init"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        issues = request.POST["issues"]

        obj = Feedback.objects.create(name=name, student_id=student_id, adviser_init=adviser_init, phone=phone,
                                      email=email, issues=issues)
        obj.save()
        try:
            subject = 'Student Feedback'
            message = "Mail from Student ID:" + student_id + "\nIssue:" + issues + ""
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [get_mail])
            messages.success(request, 'Your issue has been sent to our admin. '
                                      'Check feedback status for update. Thank You!')
        except:
            messages.error(request, 'Feedback Saved but not send to admin.')
    context = {
        'status': status
    }
    return render(request, 'feedback/feedback.html', context)
