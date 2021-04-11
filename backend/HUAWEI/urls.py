from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls import url
from .views import submit_views, site_views, user_views, eq_views

ROUTER = DefaultRouter()
ROUTER.register('user/register', user_views.UserViewSet, basename='register')

urlpatterns = [
    url('^user/profile/$', user_views.UserProfileView.as_view(), name='profile'),
    url('^user/edit/$', user_views.UserProfileView.as_view(), name='edit'),
    url(r'^site/$', site_views.SiteView.as_view(), name='site'),
    url('^user/token/$', user_views.TokenObtainView.as_view(), name='token'),
    url('^user/refresh/$', TokenRefreshView.as_view(), name='refresh'),
    url(r'^site/(?P<pk>[0-9]+)/$', site_views.SiteDetailView.as_view(), name='site_detail'),
    url(r'^equipment/(?P<pk>[0-9]+)/$', eq_views.EquipmentView.as_view(), name='equipment'),
] + ROUTER.urls
