from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.RESTRICT
    )
    email = models.EmailField()
    idade = models.IntegerField()
    sexo = models.BooleanField()
