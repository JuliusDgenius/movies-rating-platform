from django.urls import path, include
from rest_framework_nested import routers
from .views import RegisterView, UserViewSet, EmailTokenObtainPairView
from apps.ratings.views import UserRatingsViewSet

router = routers.DefaultRouter(trailing_slash='')
router.register(r'users', UserViewSet)

user_ratings_router = routers.NestedDefaultRouter(router, r'users', lookup='user', trailing_slash='')
user_ratings_router.register(r'ratings', UserRatingsViewSet, basename='user-ratings')

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', EmailTokenObtainPairView.as_view(), name='email_token_obtain_pair'),
    path('', include(router.urls)),
    path('', include(user_ratings_router.urls)),
]
