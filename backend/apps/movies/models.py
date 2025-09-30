from django.db import models
from django.conf import settings

class Movie(models.Model):
    """
    Represents a movie in the database.
    """
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    description = models.TextField(blank=True, null=True) # Optional as per spec

    # Tracking who created the movie and when
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, # Keep movie even if creator account is deleted
        null=True,
        related_name='movies_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Denormalized fields for efficient rating lookups, as suggested in the assessment
    ratings_count = models.IntegerField(default=0)
    ratings_avg = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

