from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class CareerForm(forms.Form):
    title = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "shadow",
                "placeholder": "Nombre de la carrera...",
                "autocomplete": "off",
            }
        ),
    )
    number_of_subjects = forms.IntegerField(
        required=True,
        validators=[MaxValueValidator(100), MinValueValidator(1)],
        widget=forms.NumberInput(
            attrs={
                "class": "shadow",
                "min": 1,
                "max": 99,
                "autocomplete": "off",
                "placeholder": 43,
            }
        ),
        label="Cantidad de materias",
    )
    university = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "shadow",
                "placeholder": "Nombre de la Universidad...",
                "autocomplete": "off",
            }
        ),
    )
    duration = forms.DecimalField(
        required=True,
        max_digits=3,
        decimal_places=1,
        help_text="Por ejemplo: 3,5 (tres años y medio)",
        widget=forms.NumberInput(
            attrs={
                "class": "shadow",
                "min": 1,
                "max": 99,
                "autocomplete": "off",
                "placeholder": 3.5,
            }
        ),
        label="Duración de la carrera",
    )
