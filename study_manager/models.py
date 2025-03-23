from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.CharField(
        max_length=100, help_text="Ejemplo: Martes 14a18hs, Ma14a18, etc."
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Absence(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="absences")
    date = models.DateField()
    reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.course.name} - {self.date}"


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="exams")
    date = models.DateField()
    description = models.CharField(max_length=355, blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.course.name} - {self.date} - {self.description}"
