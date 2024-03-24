from django.urls import path
from .views.views import study
from .views.publication_views import *
from .views.subject_views import *
from .views.career_views import *


app_name = "apuntes"

urlpatterns = [
    # pagina inicial, donde aparece el listado de carreras y materias
    path("", study, name="hub"),
    # pagina para ver las publicaciones de determinada materia (id) de la carrera (title)
    # CAREER REQUESTS
    path("career/", add_career, name="add_career"),
    path("career/delete/<int:pk>", delete_career, name="delete_career"),
    path("<str:career_title>/update/<int:pk>", update_career, name="update_career"),
    # SUBJECT REQUEST
    path("career/subject/", add_subject, name="add_subject"),
    path(
        "<int:career>/<str:subject_name>/delete/<int:pk>",
        delete_subject,
        name="delete_subject",
    ),
    path(
        "<int:career>/<str:subject>/update/<int:pk>",
        update_subject,
        name="update_subject",
    ),
    # USANDO CLASESS GENERICAS
    path(
        "<str:subject>/<int:id>/publicaciones",
        PublicationsListView.as_view(),
        name="publications",
    ),
    path(
        "<str:subject>/<int:id>/publicacion/",
        PublicationCreateView.as_view(),
        name="publication_create",
    ),
    path(
        "<str:subject>/<int:id>/publicacion/<int:pk>",
        PublicationDetailView.as_view(),
        name="publication_detail",
    ),
    path(
        "<str:subject>/<int:id>/publicacion/<int:pk>/update",
        PublicationUpdateView.as_view(),
        name="publication_update",
    ),
    path(
        "<str:subject>/<int:id>/publicacion/<int:pk>/delete",
        PublicationDeleteView.as_view(),
        name="publication_delete",
    ),
]
