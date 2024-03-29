from django import forms

from study_hub.models import Career, Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "code", "career"]

    name = forms.CharField(
        max_length=40,
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control my-2 ",
                "placeholder": "Nombre de la Materia",
                "autocomplete": "off",
            },
        ),
    )
    code = forms.IntegerField(
        required=True,
        label="",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control my-2 ",
                "autocomplete": "off",
                "placeholder": "Código",
                "min": 1,
                "max": 9999,
            }
        ),
    )
    career = forms.ModelChoiceField(
        queryset=Career.objects.all(),
        empty_label="Seleccione una carrera",
        label="",
        widget=forms.Select(attrs={"class": "form-control my-2"}),
    )
