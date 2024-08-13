from django.urls import path,include
from rest_framework import routers 
from .views import MovieViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
  
# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]