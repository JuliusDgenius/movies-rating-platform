from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from apps.movies.models import Movie
from apps.ratings.models import Rating

User = get_user_model()

class MovieAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        self.movie = Movie.objects.create(
            title='Pulp Fiction',
            genre='Crime',
            release_year=1994,
            created_by=self.user
        )

    def test_create_movie(self):
        """
        Ensure we can create a new movie object.
        """
        url = '/api/movies'
        data = {
            'title': 'Inception',
            'genre': 'Sci-Fi',
            'release_year': 2010,
            'description': 'A mind-bending thriller.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)
        movie = Movie.objects.get(id=response.data['id'])
        self.assertEqual(movie.title, 'Inception')
        self.assertEqual(movie.created_by, self.user)

    def test_create_rating(self):
        """
        Ensure we can create a rating for a movie.
        """
        url = f'/api/movies/{self.movie.id}/ratings'
        data = {'rating': 5, 'review': 'Classic!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.ratings_count, 1)
        self.assertEqual(self.movie.ratings_avg, 5.0)

    def test_update_rating(self):
        """
        Ensure we can update an existing rating.
        """
        rating = Rating.objects.create(movie=self.movie, user=self.user, rating=4)
        url = f'/api/movies/{self.movie.id}/ratings/{rating.id}'
        data = {'rating': 5, 'review': 'Actually, it is a classic!'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.ratings_count, 1)
        self.assertEqual(self.movie.ratings_avg, 5.0)

    def test_list_movies(self):
        """
        Ensure we can list movies with filtering.
        """
        Movie.objects.create(title='The Dark Knight', genre='Action', release_year=2008, created_by=self.user)
        url = '/api/movies?genre=Action'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.data['items'][0]['title'], 'The Dark Knight')
