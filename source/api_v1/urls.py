from django.urls import path, include

from api_v1.views import photo_view, FavoritesView

app_name = "api_v1"

urls_photos = [
    path("", photo_view, name="photo_view")
]

urlpatterns = [
    # path("echo/", echo_view),
    # path("get-token/", get_token_view),
    path("photos/", include(urls_photos)),
    path("likes/<int:pk>/", FavoritesView.as_view(), name="favorites")
]
