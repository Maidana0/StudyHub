from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course, Absence, Exam
from .forms import CourseForm, AbsenceForm, ExamForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.filter(user=self.request.user)


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = "course_form.html"
    success_url = reverse_lazy("course_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "course_form.html"
    success_url = reverse_lazy("course_list")


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = "course_confirm_delete.html"
    success_url = reverse_lazy("course_list")


class AbsenceListView(LoginRequiredMixin, ListView):
    model = Absence
    template_name = "absence_list.html"
    context_object_name = "absences"

    def get_queryset(self):
        course = Course.objects.get(pk=self.kwargs["course_id"], user=self.request.user)
        return Absence.objects.filter(course=course)


class AbsenceCreateView(LoginRequiredMixin, CreateView):
    model = Absence
    form_class = AbsenceForm
    template_name = "absence_form.html"

    def form_valid(self, form):
        form.instance.course = Course.objects.get(
            pk=self.kwargs["course_id"], user=self.request.user
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "absence_list", kwargs={"course_id": self.kwargs["course_id"]}
        )


class AbsenceDeleteView(LoginRequiredMixin, DeleteView):
    model = Absence
    template_name = "absence_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy(
            "absence_list", kwargs={"course_id": self.kwargs["course_id"]}
        )


class ExamListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = "exam_list.html"
    context_object_name = "exams"

    def get_queryset(self):
        course = Course.objects.get(pk=self.kwargs["course_id"], user=self.request.user)
        return Exam.objects.filter(course=course)


class ExamCreateView(LoginRequiredMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = "exam_form.html"

    def form_valid(self, form):
        form.instance.course = Course.objects.get(
            pk=self.kwargs["course_id"], user=self.request.user
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("exam_list", kwargs={"course_id": self.kwargs["course_id"]})


class ExamDeleteView(LoginRequiredMixin, DeleteView):
    model = Exam
    template_name = "exam_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("exam_list", kwargs={"course_id": self.kwargs["course_id"]})
