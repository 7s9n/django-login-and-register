from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from os import path


def get_profile_picture_filepath(instance, filename):
    filename = filename.split('.')[-1]
    return path.join('profile_images', '{}profile_image.{}'.format(instance.pk, filename))


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        _('profile picture'), upload_to=get_profile_picture_filepath, null=True, blank=True)
    bio = models.TextField(_('Bio'), max_length=500, blank=True)
    short_bio = models.TextField(_('Short Bio'), max_length=250, blank=True)
    source = models.CharField(_('source'), max_length=50, blank=True)


class OtpCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.code
