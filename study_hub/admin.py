from django.contrib import admin
from .models import Career, Comment, Subject, Publication


# Register your models here.
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("title", "number_of_subjects", "university")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "career")


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "subject")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("publication", "author")
