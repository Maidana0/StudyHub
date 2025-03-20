from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from study_manager.views.base_views import CourseContext
from ..models import Course, Absence, Exam
from ..forms import CourseForm, AbsenceForm, ExamForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "course_list.html"
    context_object_name = "courses"
    extra_context = {"title": "Mis Cursos"}

    def get_queryset(self):
        return Course.objects.filter(user=self.request.user)


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


class AbsenceListView(CourseContext, LoginRequiredMixin, ListView):
    model = Absence
    template_name = "absence_list.html"
    context_object_name = "absences"
    title = "Faltas"

    def get_queryset(self):
        course = Course.objects.get(pk=self.kwargs["course_id"], user=self.request.user)
        course = Absence.objects.filter(course=course).order_by("date")
        self.extra_context = {"quantity": course.__len__()}
        return course


class AbsenceCreateView(CourseContext, LoginRequiredMixin, CreateView):
    model = Absence
    form_class = AbsenceForm
    template_name = "form.html"
    title = "Anotar Falta"

    def form_valid(self, form):
        form.instance.course = Course.objects.get(
            pk=self.kwargs["course_id"], user=self.request.user
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "study_manager:absence_list", kwargs={"course_id": self.kwargs["course_id"]}
        )


class AbsenceDeleteView(CourseContext, LoginRequiredMixin, DeleteView):
    model = Absence
    template_name = "absence_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "study_manager:absence_list", kwargs={"course_id": self.kwargs["course_id"]}
        )


class ExamListView(CourseContext, LoginRequiredMixin, ListView):
    model = Exam
    template_name = "exam_list.html"
    context_object_name = "exams"
    title = "Exámenes"

    def get_queryset(self):
        course = Course.objects.get(pk=self.kwargs["course_id"], user=self.request.user)
        course_exams = Exam.objects.filter(course=course).order_by("date")
        self.extra_context = {"pending": course_exams.filter(grade=None).count()}
        return course_exams


class ExamCreateView(CourseContext, LoginRequiredMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = "form.html"
    title = "Agendar Examen"

    def form_valid(self, form):
        form.instance.course = Course.objects.get(
            pk=self.kwargs["course_id"], user=self.request.user
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "study_manager:exam_list", kwargs={"course_id": self.kwargs["course_id"]}
        )


class ExamDeleteView(CourseContext, LoginRequiredMixin, DeleteView):
    model = Exam
    template_name = "exam_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "study_manager:exam_list", kwargs={"course_id": self.kwargs["course_id"]}
        )


class ExamUpdateView(CourseContext, LoginRequiredMixin, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = "form.html"
    title = "Editar Examen"

    def form_valid(self, form):
        form.instance.course = Course.objects.get(
            pk=self.kwargs["course_id"], user=self.request.user
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "study_manager:exam_list", kwargs={"course_id": self.kwargs["course_id"]}
        )
