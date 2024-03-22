from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from study_hub.models import Publication
from django.urls import reverse_lazy
from .views import get_subject_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class PublicationsListView(ListView):
    model = Publication
    template_name = "list_publications.html"
    context_object_name = "publications"
    # extra_context = {para agregar un parametro del contexto desde la clase}

    # realizo el filtrado obteniendo la query id
    def get_queryset(self):
        return Publication.objects.filter(subject=self.kwargs["id"])

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

        context["id"] = subject.id
        context["title"] = subject.name
        return context


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    fields = ["title", "sub_title", "content", "subject", "image"]
    template_name = "publication.html"

    def get_success_url(self):
        return reverse_lazy(
            "apuntes:publication_detail",
            kwargs={
                "subject": self.kwargs["subject"],
                "id": self.kwargs["id"],
                "pk": self.object.pk,
            },
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_subject_or_404(self.kwargs["id"], self.kwargs["subject"])
        context["id"] = subject.id
        context["title"] = subject.name
        return context


class PublicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Publication
    template_name = "publication.html"
    fields = ["title", "sub_title", "content", "subject", "image"]

    def get_success_url(self):
        return reverse_lazy(
            "apuntes:publication_detail",
            kwargs={
                "subject": self.kwargs["subject"],
                "id": self.kwargs["id"],
                "pk": self.object.pk,
            },
        )

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
