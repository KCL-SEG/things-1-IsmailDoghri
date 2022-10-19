from django.db.models import Model

class Thing(Model):
    name = CharField(
        unique=True,
        blank=False
    )
    description = TextField(
        unique=False,
        blank=True
    )
    quantity = IntegerField(
        unique=False,
        blank=False
    )
