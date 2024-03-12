from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.shortcuts import redirect, render, get_object_or_404

from .forms.subject import SubjectForm
from .forms.career import CareerForm

from .models import Career, Subject, Publication

from django.views.decorators.http import require_POST, require_GET

from django.contrib import messages


# INDEX STUDYHUB
@require_GET
def study(request):
    careers = Career.objects.all().order_by("university")
    subjects = Subject.objects.all().order_by("code")

    query = request.GET.get("career", None)
    career_filter = False

    if query:
        career_filter = Career.objects.filter(id=query)

    careerForm = CareerForm()
    subjectForm = SubjectForm()

    return render(
        request,
        "study.html",
        {
            "title": "Apuntes",
            "careers": careers,
            "career_filter": career_filter,
            "subjects": subjects,
            # FORMS
            "careerForm": careerForm,
            "subjectForm": subjectForm,
        },
    )


# CAREER
@require_POST
def add_career(request):
    careerForm = CareerForm(request.POST)
    if careerForm.is_valid():
        newCareer = Career(
            title=careerForm.cleaned_data.get("title"),
            number_of_subjects=careerForm.cleaned_data.get("number_of_subjects"),
            university=careerForm.cleaned_data.get("university"),
            duration=careerForm.cleaned_data.get("duration"),
        )
        newCareer.save()
        return redirect(reverse_lazy("apuntes:hub"))
    return redirect(reverse_lazy("inicio"))


# SUBJECT
@require_POST
def add_subject(request):
    subjectForm = SubjectForm(request.POST)
    if subjectForm.is_valid():
        description = subjectForm.cleaned_data.get("description")
        newSubject = Subject(
            name=subjectForm.cleaned_data.get("name"),
            code=subjectForm.cleaned_data.get("code"),
            description=description if description else "",
            career=subjectForm.cleaned_data.get("career"),
        )
        newSubject.save()
        return redirect(reverse_lazy("apuntes:hub"))

    return redirect(reverse_lazy("inicio"))


# PUBLICATIONS GENERIC VIEW
# LISTA FILTRADA
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


class PublicationCreateView(CreateView):
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


class PublicationUpdateView(UpdateView):
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


class PublicationDeleteView(DeleteView):
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


def get_subject_or_404(id, name):
    return get_object_or_404(Subject, pk=id, name=name)
