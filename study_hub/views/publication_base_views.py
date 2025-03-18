from study_hub.models import Publication
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import EmptyPage, PageNotAnInteger
from urllib.parse import urlencode
from django.urls import reverse_lazy


def _success_url(self):
    base_url = reverse_lazy(
        "apuntes:publication_detail",
        kwargs={
            "subject": self.kwargs["subject"],
            "id": self.kwargs["id"],
            "pk": self.object.pk,
        },
    )
    query_params = urlencode({"publicacion": "nueva"})
    return f"{base_url}?{query_params}"


class PublicationTemplateNameMixin:
    template_name = "publication.html"


class PaginatedListView(ListView):
    context_object_name = "publications"
    model = Publication
    paginate_by = 10

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(queryset, page_size)
        page = self.request.GET.get("page")

        try:
            page_number = int(page)
        except (TypeError, ValueError):
            page_number = 1

        try:
            page_obj = paginator.page(page_number)
        except (EmptyPage, PageNotAnInteger):
            page_obj = paginator.page(paginator.num_pages)

        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())


class CreateViewWithSuccessURL(PublicationTemplateNameMixin, CreateView):
    model = Publication

    def get_success_url(self):
        return _success_url(self)


class UpdateViewWithSuccessURL(PublicationTemplateNameMixin, UpdateView):
    model = Publication

    def get_success_url(self):
        return _success_url(self)


class DeleteViewWithSuccessURL(PublicationTemplateNameMixin, DeleteView):
    model = Publication

    def get_success_url(self):
        return reverse_lazy(
            "apuntes:publications",
            kwargs={"subject": self.kwargs["subject"], "id": self.kwargs["id"]},
        )
