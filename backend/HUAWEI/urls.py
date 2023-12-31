from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls import url
from .views import site_views, user_views, eq_views, flow_views, assign_views, flow_generate_view, ssid_views,\
    top_views, mail_views, ticket_views, fee_views

ROUTER = DefaultRouter()
ROUTER.register('user/register', user_views.UserViewSet, basename='user')

urlpatterns = [
    url('^user/profile/$', user_views.UserProfileView.as_view(), name='profile'),
    url('^user/edit/$', user_views.UserProfileView.as_view(), name='edit'),
    url('^user/token/$', user_views.TokenObtainView.as_view(), name='token'),
    url('^user/refresh/$', TokenRefreshView.as_view(), name='refresh'),
    url('^mail/$', mail_views.MailSendView.as_view(), name='mail'),
    url(r'^fee/$', fee_views.FeeView.as_view(), name='fee'),
    url(r'^site/$', site_views.SiteView.as_view(), name='site'),
    url(r'^site/(?P<pk>[0-9]+)/$', site_views.SiteDetailView.as_view(), name='site_detail'),
    url(r'^assign/(?P<pk>[0-9]+)/$', assign_views.AssignView.as_view(), name='assign'),
    url(r'^equipment/(?P<pk>[0-9]+)/$', eq_views.EquipmentView.as_view(), name='equipment'),
    url(r'^flow/$', flow_views.TotalFlowView.as_view(), name='total_flow'),
    url(r'^flow/(?P<pk>[0-9]+)/$', flow_views.SiteFlowView.as_view(), name='site_flow'),
    url(r'^topflow/', top_views.TopSiteView.as_view(), name='top_site_flow'),
    url(r'^flowgenerate/$', flow_generate_view.FlowGenerateView.as_view(), name='flow_generate'),
    url(r'^ssid/(?P<pk>[0-9]+)/$', ssid_views.SSIDView.as_view(), name='ssid'),
    url(r'^ticket/$', ticket_views.TicketView.as_view(), name='ticket'),
] + ROUTER.urls
