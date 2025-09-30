from django.urls import path, include
from rest_framework_nested import routers
from .views import MovieViewSet
from apps.ratings.views import RatingViewSet

router = routers.DefaultRouter(trailing_slash='')
router.register(r'movies', MovieViewSet)

ratings_router = routers.NestedDefaultRouter(router, r'movies', lookup='movie', trailing_slash='')
ratings_router.register(r'ratings', RatingViewSet, basename='movie-ratings')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(ratings_router.urls)),
]
