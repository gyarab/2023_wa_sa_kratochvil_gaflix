from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)

class DirectorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Director, DirectorAdmin)

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenreAdmin)

class ActorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Actor, ActorAdmin)