from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")

    class Meta:
        abstract = True


class Photo(BaseModel):
    photo = models.ImageField(upload_to="photos", null=False, blank=False, verbose_name="Photo")
    caption = models.CharField(max_length=100, null=False, blank=False, verbose_name="Caption")
    author = models.ForeignKey(get_user_model(), related_name="photos", verbose_name="Author", default=1,
                               on_delete=models.SET_DEFAULT)
    album = models.ManyToManyField("webapp.Photo", related_name="photos", blank=True)
    is_private = models.BooleanField(blank=True, default=False)
    photo_favorites = models.ManyToManyField(get_user_model(), related_name="photo_favorites", blank=True)

    def get_absolute_url(self):
        return reverse("webapp:photo_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "photos"
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


class Album(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Name")
    description = models.TextField(max_length=3000, verbose_name="Description")
    author = models.ForeignKey(get_user_model(), related_name="albums", verbose_name="Author", default=1,
                               on_delete=models.CASCADE)
    is_private = models.BooleanField(blank=True, default=False)
    album_favorites = models.ManyToManyField(get_user_model(), related_name="album_favorites", blank=True)

    def get_absolute_url(self):
        return reverse("webapp:album_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "albums"
        verbose_name = "Album"
        verbose_name_plural = "Albums"
