from django import forms
from tinymce.widgets import TinyMCE
from ..models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {"comment": TinyMCE(attrs={"id": "id_comment", "name": "comment"})}
