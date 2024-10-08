from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from study_hub.forms.comment import CommentForm
from study_hub.models import Publication
from django.urls import reverse_lazy
from .views import get_subject_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Comment
from urllib.parse import urlencode


def _success_url(self):
    base_url = reverse_lazy(
        "apuntes:publication_detail",
        kwargs={
            "subject": self.kwargs["subject"],
            "id": self.kwargs["id"],
            "pk": self.object.pk,
        },
    )
    query_params = urlencode({"publicacion": "nueva"})
    return f"{base_url}?{query_params}"


class PublicationsListView(ListView):
    model = Publication
    template_name = "list_publications.html"
    context_object_name = "publications"
    paginate_by = 10

    # realizo el filtrado obteniendo la query id
    def get_queryset(self):
        publications_filter = Publication.objects.filter(subject=self.kwargs["id"])
        return publications_filter.order_by("-publication_date")

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


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    fields = ["title", "author", "content", "subject"]
    template_name = "publication.html"

    def get_success_url(self):
        return _success_url(self)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_subject_or_404(self.kwargs["id"], self.kwargs["subject"])
        context["id"] = subject.id
        context["title"] = subject.name
        return context


class PublicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Publication
    template_name = "publication.html"
    fields = ["title", "author", "content", "subject"]

    def get_success_url(self):
        return _success_url(self)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_subject_or_404(self.kwargs["id"], self.kwargs["subject"])

        context["id"] = subject.id
        context["title"] = subject.name
        return context


class PublicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Publication
    template_name = "publication.html"
    context_object_name = "publication"

    def get_success_url(self):
        return reverse_lazy(
            "apuntes:publications",
            kwargs={"subject": self.kwargs["subject"], "id": self.kwargs["id"]},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_subject_or_404(self.kwargs["id"], self.kwargs["subject"])

        context["id"] = subject.id
        context["title"] = subject.name
        context["delete"] = True
        context["form"] = False
        return context


#  LA IDEA VA A SER OBTENER TODAS LAS PUBLICACIONES
class AllPublicationsListView(ListView):
    model = Publication
    template_name = "all_publications.html"
    context_object_name = "publications"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Publicaciones"
        return context
