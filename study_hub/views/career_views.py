from django.views.decorators.http import require_POST
from study_hub.forms.career import CareerForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Career


@login_required
@require_POST
def add_career(request):
    career_form = CareerForm(request.POST)
    if career_form.is_valid():
        career_form.save()
        title = career_form.cleaned_data.get("title")
        messages.success(request, f"La carrera: {title}, ha sido agregada correctamente!")
        return redirect(reverse_lazy("apuntes:hub"))

    msg = f"Ocurrio un error al intentar agregar la carrera, intentelo nuevamente."
    messages.error(request, msg)
    return redirect(reverse_lazy("apuntes:hub"))


@login_required
def delete_career(request, pk):
    career = get_object_or_404(Career, pk=pk)
    if request.user.is_authenticated and request.user.is_staff:
        career.delete()
        msg = f"La carrera '{career.title}' de {career.university} fue borrada exitosamente."
        messages.success(request, msg)
    else:
        messages.error(request, "No tienes permiso para realizar esta acción.")

    return redirect(reverse_lazy("apuntes:hub"))


@login_required
def update_career(request, career_title, pk):
    if not request.user.is_authenticated and not request.user.is_staff:
        messages.error(request, "No tienes permiso para realizar esta acción.")
        return redirect(reverse_lazy("apuntes:hub"))

    career = get_object_or_404(Career, title=career_title, pk=pk)

    if request.method == "POST":
        form = CareerForm(request.POST, instance=career)
        if form.is_valid():
            form.save()
            msg = f"La carrera '{career_title}' de {career.university} fue editada exitosamente."
            messages.success(request, msg)
        return redirect(reverse_lazy("apuntes:hub"))

    else:
        form = CareerForm(instance=career)
        return render(
            request,
            "study.html",
            {"careerForm": form, "update": "career", "title": "Actualizar Carrera"},
        )
