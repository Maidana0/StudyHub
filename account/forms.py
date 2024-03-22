from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class CustomAuthForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(), label="Mantener sesión conectada"
    )


class CustomFields(forms.Form):
    def __init__(self, *args, **kwargs):
        required = kwargs.pop("required", True)  # Por defecto required es True
        super(CustomFields, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.required = required

    first_name = forms.CharField(
        max_length=30,
        label="Nombre",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "", "max-length": 30}
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        label="Apellido",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "", "max-length": 30}
        ),
    )
    email = forms.CharField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": ""}),
    )


class CustomRegisterForm(UserCreationForm, CustomFields):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "email",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email


class CustomProfileForm(CustomFields, forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "avatar",
            "first_name",
            "last_name",
            "email",
        ]

    def save(self, commit=True):
        profile_instance = super(CustomProfileForm, self).save(commit=False)
        user_instance = profile_instance.user
        user_data = self.cleaned_data

        if any(user_data[field] for field in ["first_name", "last_name", "email"]):
            user_instance.first_name = self.cleaned_data["first_name"]
            user_instance.last_name = self.cleaned_data["last_name"]
            user_instance.email = self.cleaned_data["email"]
            user_instance.save()

        if commit:
            profile_instance.save()
        return profile_instance
