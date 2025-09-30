from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter
from .pagination import MoviePagination
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter
    pagination_class = MoviePagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
