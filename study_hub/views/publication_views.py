from django.views.generic import DetailView
from study_hub.forms.comment import CommentForm
from study_hub.models import Publication
from .views import get_subject_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Comment
from django.db.models import Q
from .publication_base_views import (
    DeleteViewWithSuccessURL,
    PaginatedListView,
    CreateViewWithSuccessURL,
    UpdateViewWithSuccessURL,
)


def _filterPrivatePublications(request, queryset):
    # filtrar publicaciones privadas que no pertenecen al usuario actual
    if not request.user.is_authenticated:
        queryset = queryset.filter(isPrivate=False)
    else:
        queryset = queryset.filter(Q(isPrivate=False) | Q(author=request.user))

    return queryset.order_by("-publication_date")


class PublicationsListView(PaginatedListView):
    template_name = "list_publications.html"

    # realizo el filtrado obteniendo la query id
    def get_queryset(self):
        queryset = Publication.objects.filter(subject=self.kwargs["id"])
        return _filterPrivatePublications(self.request, queryset)

    # agrego valores al contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_subject_or_404(self.kwargs["id"], self.kwargs["subject"])

        context["subject"] = subject
        context["title"] = subject.name
        return context


class PublicationDetailView(DetailView):
    model = Publication
    template_name = "publication.html"
    context_object_name = "publication"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_subject_or_404(self.kwargs["id"], self.kwargs["subject"])
        comments = Comment.objects.filter(publication=self.kwargs["pk"])
        query_params = self.request.GET.get("publicacion", False)

        context["is_new"] = query_params
        context["id"] = subject.id
        context["title"] = subject.name
        context["comments"] = comments
        context["new_comment"] = CommentForm()
        return context


class PublicationCreateView(LoginRequiredMixin, CreateViewWithSuccessURL):
    fields = ["title", "author", "content", "subject", "isPrivate"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_subject_or_404(self.kwargs["id"], self.kwargs["subject"])
        context["id"] = subject.id
        context["title"] = subject.name
        return context


class PublicationUpdateView(LoginRequiredMixin, UpdateViewWithSuccessURL):
    fields = ["title", "author", "content", "subject", "isPrivate"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_subject_or_404(self.kwargs["id"], self.kwargs["subject"])

        context["id"] = subject.id
        context["title"] = subject.name
        return context


class PublicationDeleteView(LoginRequiredMixin, DeleteViewWithSuccessURL):
    context_object_name = "publication"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_subject_or_404(self.kwargs["id"], self.kwargs["subject"])

        context["id"] = subject.id
        context["title"] = subject.name
        context["delete"] = True
        context["form"] = False
        return context


#  OBTENER TODAS LAS PUBLICACIONES
class AllPublicationsListView(PaginatedListView):
    template_name = "all_publications.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Publicaciones"
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return _filterPrivatePublications(self.request, queryset)
