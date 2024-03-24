from django.shortcuts import render, get_object_or_404
from ..forms.subject import SubjectForm
from ..forms.career import CareerForm
from ..models import Career, Subject


def get_subject_or_404(id, name):
    return get_object_or_404(Subject, pk=id, name=name)


# INDEX STUDYHUB
def study(request):
    careers = Career.objects.all().order_by("university")
    subjects = Subject.objects.all().order_by("code")
    list = careers
    query = request.GET.get("career", None)
    if query:
        careers = Career.objects.filter(id=query)

    careerForm = CareerForm()
    subjectForm = SubjectForm()

    return render(
        request,
        "study.html",
        {
            "title": "Apuntes",
            "list": list,
            "careers": careers,
            "subjects": subjects,
            # FORMS
            "careerForm": careerForm,
            "subjectForm": subjectForm,
        },
    )
