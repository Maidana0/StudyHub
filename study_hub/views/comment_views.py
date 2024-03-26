from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from study_hub.forms.comment import CommentForm
from study_hub.views.views import get_subject_or_404
from ..models import Comment, Publication
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages


def _redirect_to_publication_detail(subject_obj, p_id):
    return redirect(
        reverse_lazy(
            "apuntes:publication_detail",
            kwargs={"subject": subject_obj.name, "id": subject_obj.pk, "pk": p_id},
        )
    )


@login_required
@require_POST
def add_comment(request, subject, s_id, p_id):
    subject_obj = get_subject_or_404(s_id, subject)
    publication = get_object_or_404(Publication, pk=p_id)
    comment = request.POST["comment"].strip()

    if len(comment) > 1:
        Comment.objects.create(
            author=request.user, publication=publication, comment=comment
        )

    return _redirect_to_publication_detail(subject_obj, p_id)


@login_required
def delete_comment(request, subject, s_id, p_id, pk):
    comment = get_object_or_404(Comment, pk=pk, publication=p_id)
    subject_obj = get_subject_or_404(s_id, subject)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Tu comentario ha sido eliminado!")
    else:
        messages.error(request, "No puedes eliminar un comentario de otra persona!")

    return _redirect_to_publication_detail(subject_obj, p_id)


@login_required
def update_comment(request, subject, s_id, p_id, pk):
    comment_obj = get_object_or_404(Comment, pk=pk, publication=p_id)
    subject_obj = get_subject_or_404(s_id, subject)
    publication_obj = get_object_or_404(Publication, pk=p_id)

    if request.method == "POST" and comment_obj.author == request.user:
        comment_form = CommentForm(request.POST, instance=comment_obj)
        if comment_form.is_valid:
            comment_form.save()
            messages.success(request, "Tu comentario ha sido actualizado correctamente!")

        return _redirect_to_publication_detail(subject_obj, p_id)

    comment_form = CommentForm(instance=comment_obj)

    return render(
        request,
        "publication.html",
        {
            "id": subject_obj.id,
            "title": subject_obj.name,
            "comments": Comment.objects.filter(publication=p_id),
            "new_comment": CommentForm(),
            "edit_comment_form": comment_form,
            "id_comment_form": comment_obj.pk,
            "publication": publication_obj,
        },
    )
