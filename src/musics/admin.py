from django.contrib import admin
from .models import Album, Band, Song, Comment


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'band', 'release_date')
    list_filter = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'album')
    list_filter = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Band)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'album', 'created', 'active')
    list_filter = ('active', 'updated', 'created')
    search_fields = ('email', 'name', 'body')
