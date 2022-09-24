from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["photo", "caption", "album", "is_private"]
        widgets = {
            "caption": widgets.Textarea(attrs={"placeholder": "Add caption"})
        }


class PhotoDeleteForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["caption"]

    def clean_caption(self):
        caption = self.cleaned_data.get("caption")
        if self.instance.caption != caption:
            raise ValidationError("Captions do not match")
        return caption


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name", "description", "is_private"]
        widgets = {
            "description": widgets.Textarea(attrs={"placeholder": "Add description"})
        }


class AlbumDeleteForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name"]

    def clean_caption(self):
        name = self.cleaned_data.get("name")
        if self.instance.name != name:
            raise ValidationError("Names do not match")
        return name

