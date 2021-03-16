from django.urls import path
from . import views, submit_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView


ROUTER = DefaultRouter()
ROUTER.register('register', views.UserViewSet, basename='user')

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('user/', views.UserOperationView.as_view(), name='user_operation'),
    path('submit/', submit_views.SubmitOrderView.as_view(), name='create_site'),
    path('token/', views.TokenObtainView.as_view(), name='auth'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
] + ROUTER.urls
