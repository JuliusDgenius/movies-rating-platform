from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Rating(models.Model):
    """
    Represents a rating given by a user to a movie.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField(blank=True, null=True) # Optional as per spec

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # A user can only rate a specific movie once.
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username}'s {self.rating}-star rating for {self.movie.title}"

