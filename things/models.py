from django.db.models import Model
from django.db import models

class Thing(Model):
    name = models.CharField(
        unique=True,
        blank=False
    )
    description = models.TextField(
        unique=False,
        blank=True
    )
    quantity = models.IntegerField(
        unique=False,
        blank=False
    )
