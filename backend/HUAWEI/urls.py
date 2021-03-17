from django.urls import path
from . import views, submit_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView


ROUTER = DefaultRouter()
ROUTER.register('user/register', views.UserViewSet, basename='user')

urlpatterns = [
    path('user/profile/', views.UserProfileView.as_view(), name='profile'),
    path('user/edit/', views.UserOperationView.as_view(), name='user_operation'),
    path('submit/', submit_views.SubmitOrderView.as_view(), name='create_site'),
    path('user/token/', views.TokenObtainView.as_view(), name='auth'),
    path('user/refresh/', TokenRefreshView.as_view(), name='refresh'),
] + ROUTER.urls
