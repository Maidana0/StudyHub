from django.http import JsonResponse
from ..forms import CourseForm
from django.db.models import Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Course
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "course_list.html"
    context_object_name = "courses"
    extra_context = {"title": "Mis Cursos"}

    def get_queryset(self):
        user_course = Course.objects.filter(user=self.request.user)
        user_course = user_course.annotate(
            absences_count=Count("absences"),
            pending_exams_count=Count("exams", filter=Q(exams__grade=None)),
        )
        return user_course


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = "form.html"
    extra_context = {"title": "Agregar Curso"}
    success_url = reverse_lazy("study_manager:course_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "form.html"
    success_url = reverse_lazy("study_manager:course_list")
    extra_context = {"title": "Editar Curso"}


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = "course_confirm_delete.html"
    success_url = reverse_lazy("study_manager:course_list")
    extra_context = {"title": "Eliminar Curso"}


@login_required
@require_POST
def toggle_hidden_course(request, pk):
    course = get_object_or_404(Course, pk=pk, user=request.user)
    course.hidden = not course.hidden
    course.save()
    # return redirect(request.META.get("HTTP_REFERER", "redirect_if_referer_not_found"))
    return JsonResponse({"hidden": course.hidden})
