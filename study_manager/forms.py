from django import forms
from .models import Course, Absence, Exam


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "code"]


class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ["date", "reason"]


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ["date", "description", "grade"]
