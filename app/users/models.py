from django.contrib.auth.models import AbstractUser
from django.db import models

__all___ = (
    'User',
)


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.pk} {self.username}'
