from django.db import models
from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    DecimalField,
    CASCADE,
)
from django.db.models.fields.files import ImageField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Career(Model):
    title = CharField(max_length=40)
    number_of_subjects = IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    university = CharField(max_length=50)
    duration = DecimalField(
        max_digits=4,
        decimal_places=1,
        help_text="Duración de la carrera en años. Ejemplo: 3.5 (tres años y medio)",
    )

    def __str__(self):
        return self.title


class Subject(Model):
    name = CharField(max_length=40)
    code = IntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1)])
    description = TextField(max_length=300, blank=True)
    career = ForeignKey(Career, on_delete=CASCADE)

    class Meta:
        ordering = ["career", "code"]

    def __str__(self):
        return self.name


class Publication(Model):
    title = CharField(max_length=60, blank=False)
    sub_title = CharField(max_length=80, blank=False)
    content = TextField(blank=False)
    publication_date = DateTimeField(auto_now_add=True)
    subject = ForeignKey(Subject, on_delete=CASCADE, blank=False)

    image = ImageField(
        verbose_name="Imagen para tu publicación",
        upload_to="study/publication/",
        blank=True,
    )

    def __str__(self):
        return self.title
