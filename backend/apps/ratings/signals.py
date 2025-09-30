from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg

from .models import Rating

@receiver([post_save, post_delete], sender=Rating)
def update_movie_ratings(sender, instance, **kwargs):
    movie = instance.movie
    movie.ratings_count = movie.ratings.count()
    movie.ratings_avg = movie.ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    movie.save()
