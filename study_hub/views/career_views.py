from django.views.decorators.http import require_POST
from study_hub.forms.career import CareerForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required
@require_POST
def add_career(request):
    career_form = CareerForm(request.POST)
    if career_form.is_valid():
        career_form.save()
        return redirect(reverse_lazy("apuntes:hub"))
    return redirect(reverse_lazy("inicio"))
