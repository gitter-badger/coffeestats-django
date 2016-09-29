from __future__ import absolute_import

from django.conf.urls import url
from oauth2_provider import views

from .views import CoffeestatsApplicationRegistration, \
    CoffeestatsApplicationPendingApproval

urlpatterns = (
    url(r'^authorize/$', views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', views.TokenView.as_view(), name="token"),
    url(r'^revoke_token/$', views.RevokeTokenView.as_view(),
        name="revoke-token"),
)

# Application management views
urlpatterns += (
    url(r'^applications/$', views.ApplicationList.as_view(), name="list"),
    url(r'^applications/register/$',
        CoffeestatsApplicationRegistration.as_view(), name="register"),
    url(r'^applications/(?P<pk>\d+)/$', views.ApplicationDetail.as_view(),
        name="detail"),
    url(r'^applications/(?P<pk>\d+)/delete/$',
        views.ApplicationDelete.as_view(), name="delete"),
    url(r'^applications/(?P<pk>\d+)/update/$',
        views.ApplicationUpdate.as_view(), name="update"),
    url(r'^applications/(?P<pk>\d+)/pending/$',
        CoffeestatsApplicationPendingApproval.as_view(),
        name="pending_approval"),
)

urlpatterns += (
    url(r'^authorized_tokens/$', views.AuthorizedTokensListView.as_view(),
        name="authorized-token-list"),
    url(r'^authorized_tokens/(?P<pk>\d+)/delete/$',
        views.AuthorizedTokenDeleteView.as_view(),
        name="authorized-token-delete"),
)
