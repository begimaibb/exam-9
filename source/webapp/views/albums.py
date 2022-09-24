from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from webapp.forms import PhotoForm, PhotoDeleteForm, AlbumForm, AlbumDeleteForm
from webapp.models import Photo, Album
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class AlbumView(DetailView):
    template_name = "albums/album_view.html"
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['photos'] = self.object.photos.order_by("-created_at")
        return context


class CreateAlbum(LoginRequiredMixin, CreateView):
    form_class = AlbumForm
    template_name = "albums/create.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)


class UpdateAlbum(PermissionRequiredMixin, UpdateView):
    form_class = AlbumForm
    template_name = "albums/update.html"
    model = Album

    def has_permission(self):
        return self.request.user.has_perm("webapp.change_album") or \
               self.request.user == self.get_object().author


class DeleteAlbum(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = "albums/delete.html"
    success_url = reverse_lazy('webapp:index')
    form_class = AlbumDeleteForm
    permission_required = "webapp.delete_album"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=self.get_object())
        if form.is_valid():
            return self.delete(request, *args, **kwargs)
        else:
            return self.get(request, *args, **kwargs)
