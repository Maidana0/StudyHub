from django.contrib.auth import login, authenticate, logout, views as auth_views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import CustomRegisterForm, CustomAuthForm
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required


from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomProfileForm


from django.contrib.auth import update_session_auth_hash


def login_request(request):
    if request.user.is_authenticated:
        messages.success(request, "Ya esta conectado!")
        return redirect(reverse_lazy("home"))

    context = {"title": "Iniciar Sesión", "site": "login", "form": CustomAuthForm}
    form = CustomAuthForm(request, request.POST)

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(
                request,
                username=request.POST["username"],
                password=request.POST["password"],
            )
            if user is not None:
                login(request, user)
                if not form.cleaned_data.get("remember_me", False):
                    request.session.set_expiry(0)

                messages.success(request, "Sesión iniciada correctamente!")
                return redirect(reverse_lazy("home"))
        else:
            messages.error(request, "Usuario y/o contraseña incorrecto!")

    return render(request, "auth.html", context)


def register_request(request):
    if request.user.is_authenticated:
        messages.success(request, "Ya esta registrado!")
        return redirect(reverse_lazy("home"))

    context = {
        "title": "Crear cuenta nueva",
        "site": "register",
        "form": CustomRegisterForm,
    }

    if request.method == "POST":
        form = CustomRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                request,
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password1"),
            )
            login(request, user)
            messages.success(
                request,
                "Bienvenido "
                + form.cleaned_data.get("first_name")
                + ", el registro fue exitoso!",
            )
            return redirect(reverse_lazy("home"))
        else:
            messages.error(request, "Por favor, corrija los errores del formulario.")
            context.update({"form": form})

    return render(request, "auth.html", context)


@login_required
def logout_request(request):
    logout(request)
    messages.success(request, "Se ha desconectado exitosamente!")
    return redirect(reverse_lazy("home"))


@login_required
def profile_request(request):
    user = User.objects.get(username=request.user.username)
    profile = (
        Profile.objects.get(user=user)
        if Profile.objects.filter(user=user)
        else Profile.objects.create(user=user)
    )
    if request.method == "POST":
        profile_form = CustomProfileForm(
            request.POST, request.FILES, instance=profile, required=False
        )

        if profile_form.is_valid():
            profile_form.save()
            return redirect(reverse_lazy("account:profile"))
    else:
        profile_form = CustomProfileForm(
            instance=profile,
            initial={
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            },
        )

    context = {
        "title": "Mi Perfil",
        "site": "profile",
        "form": profile_form,
    }
    return render(request, "auth.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Su contraseña fue actualizada exitosamente!")
            return redirect(reverse_lazy("account:profile"))
        else:
            messages.error(request, "Por favor, corrija el o los siguientes errores.")
    else:
        form = PasswordChangeForm(request.user)
    return render(
        request,
        "auth.html",
        {"site": "change_password", "title": "Cambiar contraseña", "form": form},
    )


class CustomPasswordReset(auth_views.PasswordResetView):
    template_name = "password_reset.html"
    success_url = reverse_lazy("account:password_reset_done")
    extra_context = {"site": "password_reset"}

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")
        if User.objects.filter(email=email).exists():
            return super().post(request, *args, **kwargs)
        else:
            msg = f"No existe ningun usuario registrado con el siguiente correo electronico: {email}"
            messages.error(request, msg)
            return redirect(reverse_lazy("account:password_reset"))


class CustomPasswordResetDone(auth_views.PasswordResetDoneView):
    customMessages = [
        "Le enviamos las instrucciones para recuperar su cuenta por correo electrónico",
        """ Si no recibe un correo electrónico, asegúrese de haber ingresado la dirección con la que se
        registró y verifique su carpeta de correo no deseado.""",
    ]

    template_name = "password_reset.html"
    extra_context = {"customMessages": customMessages}


class CustomPasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = "password_reset.html"
    extra_context = {"site": "password_reset_confirm"}
    success_url = reverse_lazy("account:password_reset_complete")


class CustomPasswordResetComplete(auth_views.PasswordResetCompleteView):
    customMessages = [
        "Su contraseña ha sido restablecida exitosamente!",
        "Puede continuar e iniciar sesión ahora.",
    ]

    template_name = "password_reset.html"
    extra_context = {"customMessages": customMessages}
