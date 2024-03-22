from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404

from ..forms.subject import SubjectForm
from ..forms.career import CareerForm

from ..models import Career, Subject

from django.views.decorators.http import require_POST, require_GET

# from django.contrib import messages


def get_subject_or_404(id, name):
    return get_object_or_404(Subject, pk=id, name=name)


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
