from django.urls import path
from .views import (
    PublicationCreateView,
    PublicationDeleteView,
    PublicationDetailView,
    PublicationUpdateView,
    PublicationsListView,
    add_career,
    add_subject,
    study,
)

app_name = "apuntes"

urlpatterns = [
    # pagina inicial, donde aparece el listado de carreras y materias
    path("", study, name="hub"),
    # pagina para ver las publicaciones de determinada materia (id) de la carrera (title)
    # TODO POST METHOD
    path("career/", add_career, name="add_career"),
    path("career/subject/", add_subject, name="add_subject"),
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
