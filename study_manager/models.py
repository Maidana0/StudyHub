from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.name


class Absence(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="absences")
    date = models.DateField()
    reason = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.subject.name} - {self.date}"


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="exams")
    date = models.DateField()
    description = models.CharField(max_length=255)
    grade = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject.name} - {self.date} - {self.description}"
