from django.urls import path
from .views import *

app_name = "study_manager"

urlpatterns = [
    path("cursos/", CourseListView.as_view(), name="course_list"),
    path("cursos/add/", CourseCreateView.as_view(), name="course_add"),
    path("cursos/<int:pk>/edit/", CourseUpdateView.as_view(), name="course_edit"),
    path("cursos/<int:pk>/delete/", CourseDeleteView.as_view(), name="course_delete"),
    path(
        "cursos/<int:subject_id>/absences/",
        AbsenceListView.as_view(),
        name="absence_list",
    ),
    path(
        "cursos/<int:subject_id>/absences/add/",
        AbsenceCreateView.as_view(),
        name="absence_add",
    ),
    path(
        "cursos/<int:subject_id>/absences/<int:pk>/delete/",
        AbsenceDeleteView.as_view(),
        name="absence_delete",
    ),
    path("cursos/<int:subject_id>/exams/", ExamListView.as_view(), name="exam_list"),
    path("cursos/<int:subject_id>/exams/add/", ExamCreateView.as_view(), name="exam_add"),
    path(
        "cursos/<int:subject_id>/exams/<int:pk>/delete/",
        ExamDeleteView.as_view(),
        name="exam_delete",
    ),
]
