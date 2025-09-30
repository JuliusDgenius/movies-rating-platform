from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "genre", "release_year", "ratings_avg", "ratings_count", "created_by", "created_at")
    list_filter = ("genre", "release_year")
    search_fields = ("title",)
