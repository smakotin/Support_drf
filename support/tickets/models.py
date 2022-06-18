from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    # status choices
    TO_DO = 'to_do'
    IN_PROGRESS = 'in_progress'
    IN_REVIEW = 'in_review'
    DONE = 'done'
    CLOSED = 'closed'
    CHOICES = [
        (TO_DO, 'To do'),
        (IN_PROGRESS, 'In progress'),
        (IN_REVIEW, 'In review'),
        (DONE, 'Done'),
        (CLOSED, 'Closed'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES, default=TO_DO)

    def __str__(self):
        return self.title
