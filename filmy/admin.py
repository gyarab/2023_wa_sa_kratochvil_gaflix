from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year', 'footage', 'photo', 'director']
    list_display_links = ['id', 'title']
    search_fields = ["=id", "title", "director__name"]
    list_filter = ['year', "genres"]
    list_editable = ['year', 'footage', 'director', 'photo']

admin.site.register(Movie, MovieAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birthyear', 'photo']
    list_display_links = ['id', 'name']
    search_fields = ["=id", "name"]
    list_editable = ['birthyear', 'photo']

admin.site.register(Director, DirectorAdmin)

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenreAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birthyear', 'photo']
    list_display_links = ['id', 'name']
    search_fields = ["=id", "name"]
    list_editable = ['birthyear', 'photo']

admin.site.register(Actor, ActorAdmin)