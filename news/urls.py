from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views
app_name = 'news'

urlpatterns = [

    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),

    path('user/<int:pk>/', views.RetrieveCustomerViewSet.as_view({'get': 'retrieve'}), name='user'),

    path("", views.NewtViewSet.as_view({'get': 'list', 'post': 'create'}), name="news"),

    path("recommended/", views.RecommendationNewViewSet.as_view({'get': 'list'}), name="news"),
    path("recent/", views.RecentNewViewSet.as_view({'get': 'list'}), name="news"),
    path("category/", views.NewCategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name="new_category"),
    path("source/", views.SourceViewSet.as_view({'get': 'list', 'post': 'create'}), name="source"),
    path("news-by-category/<int:pk>/", views.NewsByCategoryViewSet.as_view({'get': 'retrieve'}), name="news-by-category"),
    path("random-news-by-category/<int:pk>/", views.RandomNewsByCategoryViewSet.as_view({'get': 'retrieve'}), name="random-news-by-category"),

]
