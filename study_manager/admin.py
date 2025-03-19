from django.contrib import admin
from .models import Course, Absence, Exam


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("user", "name")


@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ("course", "date")


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("course", "date")
