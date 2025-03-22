from datetime import date
from django import forms
from .models import Course, Absence, Exam


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "schedule"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control shadow-sm",
                    "placeholder": "Nombre del curso...",
                    "style": "border-radius: 5px; padding: 10px; font-size: 16px;",
                    "autocomplete": "off",
                },
            ),
            "schedule": forms.TextInput(
                attrs={
                    "class": "form-control shadow-sm",
                    "placeholder": "Horario de cursada...",
                    "style": "border-radius: 5px; padding: 10px; font-size: 16px;",
                    "autocomplete": "off",
                }
            ),
        }


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ["date", "reason"]
        widgets = {
            "date": forms.DateInput(
                attrs={
                    "class": "form-control shadow-sm",
                    "style": "border-radius: 5px; padding: 10px; font-size: 16px;",
                    "type": "date",
                    "value": date.today(),
                },
            ),
            "reason": forms.TextInput(
                attrs={
                    "class": "form-control shadow-sm",
                    "placeholder": "Razón de la falta (opcional)",
                    "style": "border-radius: 5px; padding: 10px; font-size: 16px;",
                    "autocomplete": "off",
                }
            ),
        }


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ["date", "description", "grade"]
        widgets = {
            "date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control shadow-sm",
                    "style": "border-radius: 5px; padding: 10px; font-size: 16px;",
                    "type": "date",
                },
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control shadow-sm",
                    "placeholder": "Descripción del examen (opcional)",
                    "style": "border-radius: 5px; padding: 10px; font-size: 16px;",
                    "autocomplete": "off",
                }
            ),
            "grade": forms.NumberInput(
                attrs={
                    "class": "form-control shadow-sm",
                    "placeholder": "Nota del examen (opcional)",
                    "style": "border-radius: 5px; padding: 10px; font-size: 16px;",
                    "min": "0",
                    "max": "10",
                    "step": "0.1",
                    "autocomplete": "off",
                }
            ),
        }
