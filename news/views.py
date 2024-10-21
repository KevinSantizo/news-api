from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView

from news.models import New, NewCategory, CustomUser, Source
from rest_framework import viewsets, status
from django.utils import timezone

from news.serializers import NewSerializer, NewCategorySerializer, MyTokenObtainPairSerializer, RegisterSerializer, \
    CustomUserSerializer, SourceSerializer, NewsByCategorySerializer, RandomNewsByCategorySerializer

from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

# Login User


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Register User


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class NewtViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = New.objects.all()
    serializer_class = NewSerializer


class NewCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = NewCategory.objects.all()
    serializer_class = NewCategorySerializer


class SourceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class RetrieveCustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Custom views

class RecommendationNewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NewSerializer

    def get_queryset(self):
        queryset = New.objects.filter(recommendation=True).order_by('-created')
        return queryset


class RecentNewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NewSerializer

    def get_queryset(self):
        queryset = New.objects.filter(created__gte=timezone.now() - timezone.timedelta(days=1)).order_by('-created')
        return queryset


class NewsByCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = NewCategory.objects.all()
    serializer_class = NewsByCategorySerializer


class RandomNewsByCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = NewCategory.objects.all()
    serializer_class = RandomNewsByCategorySerializer
    