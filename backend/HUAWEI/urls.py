from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls import url
from .views import submit_views, site_views, user_views

ROUTER = DefaultRouter()
ROUTER.register('user/register', views.UserViewSet, basename='user')

urlpatterns = [
    url('^user/profile/$', user_views.UserProfileView.as_view(), name='profile'),
    url('^user/edit/$', user_views.UserOperationView.as_view(), name='user_operation'),
    url('^submit/$', submit_views.SubmitOrderView.as_view(), name='create_site'),
    url(r'^site/$', site_views.SiteListView.as_view(), name='site_list'),
    url('^user/token/$', user_views.TokenObtainView.as_view(), name='auth'),
    yrl('^user/refresh/$', TokenRefreshView.as_view(), name='refresh'),
    #url(r'^site/(?P<pk>[0-9]+)/$', site_views.SiteDetailView.as_view(), name='site_detail'),
] + ROUTER.urls
