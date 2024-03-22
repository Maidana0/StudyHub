from django.urls import path
from .views import (
    change_password,
    login_request,
    logout_request,
    profile_request,
    register_request,
    CustomPasswordReset,
    CustomPasswordResetDone,
    CustomPasswordResetConfirm,
    CustomPasswordResetComplete,
)

app_name = "account"
password_reset_config = [
    # EMAIL
    path("restablecer-contraseña", CustomPasswordReset.as_view(), name="password_reset"),
    # MSG
    path(
        "restablecer-contraseña-enviado",
        CustomPasswordResetDone.as_view(),
        name="password_reset_done",
    ),
    # NEW_PASSWORD1 AND NEW_PASSWORD2
    path(
        "restablecer-contraseña/<uidb64>/<token>/",
        CustomPasswordResetConfirm.as_view(),
        name="password_reset_confirm",
    ),
    # MSG
    path(
        "restablecer-contraseña/finalizado",
        CustomPasswordResetComplete.as_view(),
        name="password_reset_complete",
    ),
]


urlpatterns = [
    path("iniciar-sesion/", login_request, name="login"),
    path("registrarse/", register_request, name="register"),
    path("perfil/", profile_request, name="profile"),
    path("cambiar-contraseña/", change_password, name="change_password"),
    path("cerrar-sesion/", logout_request, name="logout"),
    *password_reset_config,
]
