from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from mainproject.settings import AUTH_USER_MODEL


# Create your models here.
class Ticket(models.Model):
    NEW = 'N'
    IN_PROGRESS = 'P'
    DONE = 'D'
    INVALID = 'I'
    status_CHOICES = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    )
    title = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    usersubmited = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        related_name='usersubmitted'
    )
    status = models.CharField(
        max_length=1,
        choices=status_CHOICES,
        default=NEW
    )
    userassigned = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        related_name='userassigned',
        blank=True,
        null=True)
    usercompleted = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        related_name='usercompleted',
        blank=True,
        null=True)

    def __str__(self):
        return self.title

class Tracker(AbstractUser):
    pass