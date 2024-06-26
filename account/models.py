import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    avatar = models.ImageField(upload_to="avatars", default="avatars/default_avatar.png")

    @property
    def user_publications(self):
        return self.user.publications.all()

    def save(self, *args, **kwargs):
        if self.pk and self.avatar:
            old_profile = Profile.objects.get(pk=self.pk)

            if (
                "_avatar" in old_profile.avatar.name
                and old_profile.avatar.name != "avatars/default_avatar.png"
            ):
                # SI EL ARCHIVO YA EXISTE Y NO ES EL DETERMINADO, LO BORRO
                default_storage.delete(old_profile.avatar.path)

            # ESTO ES PARA CAMBIARLE EL NOMBRE AL AVATAR CREADO
            if self.avatar.name != "avatars/default_avatar.png":
                filename, ext = os.path.splitext(self.avatar.name)
                self.avatar.name = self.user.username + "_avatar" + ext
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}__avatar"


# CONVIERTO Y TRANSFORMO EL TAMAÑO Y EL FORMATO DE LA IMAGEN AVATAR EN PROFILE
@receiver(post_save, sender=Profile)
def resize_avatar(sender, instance, created, **kwargs):
    if not created and instance.avatar.name != "avatars/default_avatar.png":
        image_path = os.path.join(settings.MEDIA_ROOT, str(instance.avatar.name))
        img = Image.open(image_path)
        max_size = (138, 138)
        img.thumbnail(max_size)
        img.save(instance.avatar.path)


# CREO UN OBJETO PROFILE LUEGO DE QUE SE CREE UN USER
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
