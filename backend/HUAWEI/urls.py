from django.urls import path
from django.conf.urls import url
from .views import submit_views, site_views, user_views

urlpatterns = [
    url('^profile/$', user_views.UserProfileView.as_view(), name='profile'),
    url('^user/$', user_views.UserOperationView.as_view(), name='user_operation'),
    url('^submit/$', submit_views.SubmitOrderView.as_view(), name='create_site'),
    url(r'^site/$', site_views.SiteListView.as_view(), name='site_list'),
    #url(r'^site/(?P<pk>[0-9]+)/$', site_views.SiteDetailView.as_view(), name='site_detail'),
]
