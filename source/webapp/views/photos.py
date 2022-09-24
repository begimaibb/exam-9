from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from webapp.forms import PhotoForm, PhotoDeleteForm
from webapp.models import Photo, Album
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    model = Photo
    template_name = "photos/index.html"
    context_object_name = "photos"
    ordering = "-created_at"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        # context["form"] = self.form
        return context


class PhotoView(DetailView):
    template_name = "photos/photo_view.html"
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['comments'] = self.object.comments.order_by("-created_at")
        return context


class CreatePhoto(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = "photos/create.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)


class UpdatePhoto(PermissionRequiredMixin, UpdateView):
    form_class = PhotoForm
    template_name = "photos/update.html"
    model = Photo

    def has_permission(self):
        return self.request.user.has_perm("webapp.change_photo") or \
               self.request.user == self.get_object().author


class DeletePhoto(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = "photos/delete.html"
    success_url = reverse_lazy('webapp:index')
    form_class = PhotoDeleteForm
    permission_required = "webapp.delete_photo"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=self.get_object())
        if form.is_valid():
            return self.delete(request, *args, **kwargs)
        else:
            return self.get(request, *args, **kwargs)
