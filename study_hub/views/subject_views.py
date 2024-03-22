from study_hub.forms.subject import SubjectForm

from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required
@require_POST
def add_subject(request):
    subject_form = SubjectForm(request.POST)
    if subject_form.is_valid():
        subject_form.save()
        return redirect(reverse_lazy("apuntes:hub"))

    return redirect(reverse_lazy("inicio"))
