from datetime import timedelta
from secrets import token_urlsafe
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    birthday = models.DateField(null=True, blank=True, verbose_name="Birthday")
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name="Avatar")
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                verbose_name="User",
                                related_name="profile")


class Token(models.Model):
    TOKEN_LIFETIME_SECONDS = 2 * 60 * 60

    token = models.CharField(max_length=50, unique=True, default=token_urlsafe)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def is_expired(self):
        return self.created_at + timedelta(seconds=self.TOKEN_LIFETIME_SECONDS) < timezone.now()