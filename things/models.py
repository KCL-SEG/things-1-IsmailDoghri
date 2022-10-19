from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False
    )
    description = models.TextField(
        max_length=120,
        unique=False,
        blank=True
    )
    quantity = models.IntegerField(
        unique=False,
        blank=False,
        validators=[MaxValueValidator(
            limit_value=100
            ),MinValueValidator(
            limit_value=0
            )]
    )
