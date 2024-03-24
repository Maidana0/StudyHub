from study_hub.forms.subject import SubjectForm
from ..models import Subject

from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
@require_POST
def add_subject(request):
    subject_form = SubjectForm(request.POST)
    if subject_form.is_valid():
        subject_form.save()
        return redirect(reverse_lazy("apuntes:hub"))

    return redirect(reverse_lazy("inicio"))


@login_required
def delete_subject(request, career, subject_name, pk):
    if request.user.is_authenticated and request.user.is_staff:
        subject = get_object_or_404(Subject, career=career, name=subject_name, pk=pk)
        subject.delete()
        msg = f"La materia '{subject.name}' de {subject.career} fue borrada exitosamente."
        messages.success(request, msg)
    else:
        messages.error(request, "No tienes permiso para realizar esta acción.")

    return redirect(reverse_lazy("apuntes:hub"))


@login_required
def update_subject(request, career, subject, pk):
    if not request.user.is_authenticated and not request.user.is_staff:
        messages.error(request, "No tienes permiso para realizar esta acción.")
        return redirect(reverse_lazy("apuntes:hub"))

    subject_object = get_object_or_404(Subject, name=subject, career=career, pk=pk)

    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject_object)
        if form.is_valid():
            form.save()
            msg = f"La materia '{subject}' de {career} fue actualizada exitosamente."
            messages.success(request, msg)
        return redirect(reverse_lazy("apuntes:hub"))

    else:
        form = SubjectForm(instance=subject_object)
        return render(
            request,
            "study.html",
            {"subjectForm": form, "update": "subject", "title": "Actualizar Materia"},
        )
