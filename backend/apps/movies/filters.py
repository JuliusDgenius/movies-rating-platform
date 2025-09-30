import django_filters
from .models import Movie


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    genre = django_filters.CharFilter(field_name='genre', lookup_expr='iexact')
    search = django_filters.CharFilter(method='filter_search')
    year = django_filters.NumberFilter(field_name='release_year', lookup_expr='exact')
    year_from = django_filters.NumberFilter(field_name='release_year', lookup_expr='gte')
    year_to = django_filters.NumberFilter(field_name='release_year', lookup_expr='lte')
    min_rating = django_filters.NumberFilter(field_name='ratings_avg', lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name='ratings_avg', lookup_expr='lte')

    class Meta:
        model = Movie
        fields = (
            'title',
            'genre',
            'year',
            'year_from',
            'year_to',
            'min_rating',
            'max_rating',
            'search',
        )

    def filter_search(self, queryset, name, value):
        return queryset.filter(title__icontains=value)


