from study_manager.models import Course


class CourseContext:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = Course.objects.get(
            pk=self.kwargs["course_id"], user=self.request.user
        )
        if self.title:
            context["title"] = self.title + " - " + context["course"].name
        return context
