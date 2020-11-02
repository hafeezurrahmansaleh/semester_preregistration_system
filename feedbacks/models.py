from django.db import models


# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    student_id = models.CharField(max_length=255, blank=True, null=True)
    adviser_init = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    issues = models.CharField(max_length=255, blank=True, null=True)
    is_solved = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-uploaded_at',)
