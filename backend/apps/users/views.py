from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, EmailTokenObtainPairSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = EmailTokenObtainPairSerializer
