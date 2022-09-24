from django.contrib import admin

# Register your models here.
from webapp.models import Photo, Album


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'caption', 'author', 'is_private']
    list_display_links = ['caption']
    list_filter = ['author']
    search_fields = ['album', 'caption']
    fields = ['photo', 'caption', 'author', 'album', 'is_private', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Album)
admin.site.register(Photo, PhotoAdmin)