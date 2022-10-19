from django.db import models

class Thing(models.Model):
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
