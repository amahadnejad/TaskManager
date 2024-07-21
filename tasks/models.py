from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    STATUS_CHOICES = (
        ('p', 'In Progress'),
        ('d', 'Done'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=600)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=STATUS_CHOICES[0][0])
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}: {self.title}"
