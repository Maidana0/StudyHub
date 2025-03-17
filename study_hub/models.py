from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    ForeignKey,
    IntegerField,
    DecimalField,
    BooleanField,
    CASCADE,
)
from django.core.validators import MaxValueValidator, MinValueValidator
from tinymce import models as tinymce_models
from django.contrib.auth.models import User


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
    career = ForeignKey(Career, on_delete=CASCADE)

    class Meta:
        ordering = ["career", "code"]

    def __str__(self):
        return self.name


class Publication(Model):
    author = ForeignKey(User, on_delete=CASCADE, blank=False, default=1)
    title = CharField(max_length=60, blank=False)
    content = tinymce_models.HTMLField()
    publication_date = DateTimeField(auto_now_add=True)
    subject = ForeignKey(Subject, on_delete=CASCADE, blank=False)
    isPrivate = BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(Model):
    author = ForeignKey(User, on_delete=CASCADE, blank=False)
    publication = ForeignKey(Publication, on_delete=CASCADE, blank=False)
    comment = tinymce_models.HTMLField()
    comment_date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.author.username} en {self.publication.title}"
