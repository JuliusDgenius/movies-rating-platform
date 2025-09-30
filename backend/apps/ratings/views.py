from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Rating
from .serializers import RatingSerializer
from apps.movies.models import Movie

class RatingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(movie_id=self.kwargs['movie_pk'])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating = serializer.save(user=request.user, movie_id=kwargs['movie_pk'])
        
        # Get updated movie with fresh aggregates
        movie = Movie.objects.get(id=kwargs['movie_pk'])
        
        return Response({
            'rating': RatingSerializer(rating).data,
            'movie': {
                'id': movie.id,
                'ratings_avg': movie.ratings_avg,
                'ratings_count': movie.ratings_count,
            }
        }, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        rating = serializer.save()
        
        # Get updated movie with fresh aggregates
        movie = Movie.objects.get(id=kwargs['movie_pk'])
        
        return Response({
            'rating': RatingSerializer(rating).data,
            'movie': {
                'id': movie.id,
                'ratings_avg': movie.ratings_avg,
                'ratings_count': movie.ratings_count,
            }
        })

class UserRatingsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(user_id=self.kwargs['user_pk'])
