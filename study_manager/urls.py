from django.urls import path
from .views.views import *

app_name = "study_manager"

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("agregar-curso/", CourseCreateView.as_view(), name="course_add"),
    path("<int:pk>/editar-curso/", CourseUpdateView.as_view(), name="course_edit"),
    path("<int:pk>/borrar-curso/", CourseDeleteView.as_view(), name="course_delete"),
    path(
        "<int:course_id>/asistencias/",
        AbsenceListView.as_view(),
        name="absence_list",
    ),
    path(
        "<int:course_id>/asistencias/agregar/",
        AbsenceCreateView.as_view(),
        name="absence_add",
    ),
    path(
        "<int:course_id>/asistencias/<int:pk>/borrar/",
        AbsenceDeleteView.as_view(),
        name="absence_delete",
    ),
    path("<int:course_id>/examenes/", ExamListView.as_view(), name="exam_list"),
    path("<int:course_id>/examenes/agregar/", ExamCreateView.as_view(), name="exam_add"),
    path(
        "<int:course_id>/examenes/<int:pk>/editar/",
        ExamUpdateView.as_view(),
        name="exam_update",
    ),
    path(
        "<int:course_id>/examenes/<int:pk>/borrar/",
        ExamDeleteView.as_view(),
        name="exam_delete",
    ),
]
