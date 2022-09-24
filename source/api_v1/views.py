from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from datetime import datetime
import json

from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie

from webapp.models import Photo


def photo_view(request):
    print(request)
    if request.method == "GET":
        photos = Photo.objects.values("photo", "caption")
        return JsonResponse(list(photos), safe=False)
    elif request.method == "POST":
        if request.body:
            body = json.loads(request.body)
            if len(body.get("caption")) < 5:
                return JsonResponse({"message": "Error"}, status=400)
            # article = Article.objects.create(**body)
            return JsonResponse({"id": 1}, status=201)
        return JsonResponse({"message": "error"}, status=400)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


class FavoritesView(LoginRequiredMixin, View):
    def get(self, request, *args, pk, **kwargs):
        photo = Photo.objects.get(pk=pk)
        user = self.request.user
        if user in photo.photo_favorites.all():
            photo.photo_favorites.remove(user)
        else:
            photo.photo_favorites.add(user)

        return JsonResponse({"count": photo.photo_favorites.count()})
