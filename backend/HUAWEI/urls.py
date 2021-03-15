from django.urls import path
from . import views, submit_views

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('', views.UserOperationView.as_view(), name='user_operation'),
    path('submit/', submit_views.SubmitOrderView.as_view(), name='create_site'),
]
