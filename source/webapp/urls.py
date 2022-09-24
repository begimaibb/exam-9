from django.urls import path
from django.views.generic import RedirectView

from webapp.views import IndexView, CreatePhoto, PhotoView, UpdatePhoto, DeletePhoto, CreateAlbum, AlbumView, UpdateAlbum, DeleteAlbum


app_name = "webapp"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('photos/', RedirectView.as_view(pattern_name="index")),
    path('photos/add/', CreatePhoto.as_view(), name="create_photo"),
    path('photo/<int:pk>/', PhotoView.as_view(), name="photo_view"),
    path('photo/<int:pk>/update/', UpdatePhoto.as_view(), name="update_photo"),
    path('photo/<int:pk>/delete/', DeletePhoto.as_view(), name="delete_photo"),
    path('albums/add/', CreateAlbum.as_view(), name="create_album"),
    path('album/<int:pk>/', AlbumView.as_view(), name="album_view"),
    path('album/<int:pk>/update/', UpdateAlbum.as_view(), name="update_album"),
    path('album/<int:pk>/delete/', DeleteAlbum.as_view(), name="delete_album"),
]
