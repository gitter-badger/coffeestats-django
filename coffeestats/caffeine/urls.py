# -*- python -*-

from django.conf.urls import url

from .views import (
    AboutView,
    CaffeineActivationView,
    CaffeineRegistrationView,
    ConfirmActionView,
    DeleteAccountView,
    ExploreView,
    ExportActivityView,
    ImprintView,
    IndexView,
    OnTheRunOldView,
    OnTheRunView,
    OverallView,
    ProfileView,
    PublicProfileView,
    RegistrationClosedView,
    SelectTimeZoneView,
    SettingsView,
    SubmitCaffeineView,
    SubmitCaffeineOnTheRunView,
    DeleteCaffeineView,
    random_users,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    # registration
    url(r'^auth/activate/(?P<activation_key>\w+)/$',
        CaffeineActivationView.as_view(),
        name='registration_activate'),
    url(r'^auth/register/$', CaffeineRegistrationView.as_view(),
        name='registration_register'),
    url(r'^auth/register/closed$', RegistrationClosedView.as_view(),
        name='registration_disallowed'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^explore/$', ExploreView.as_view(), name='explore'),
    url(r'^imprint/$', ImprintView.as_view(), name='imprint'),
    url(r'^overall/$', OverallView.as_view(), name='overall'),
    url(r'^settings/$', SettingsView.as_view(), name='settings'),
    url(r'^selecttimezone/$', SelectTimeZoneView.as_view(),
        name='selecttimezone'),
    url(r'^ontherun/$', OnTheRunOldView.as_view(), name='ontherunold'),
    url(r'^ontherun/(?P<username>[\w0-9@.+-_]+)/(?P<token>\w+)/$',
        OnTheRunView.as_view(), name='ontherun'),
    url(r'^activity/export/$',
        ExportActivityView.as_view(),
        name='export_activity'),
    url(r'^deletemyaccount/$',
        DeleteAccountView.as_view(),
        name='delete_account'),
    url(r'^(?P<drink>(coffee|mate))/submit/$',
        SubmitCaffeineView.as_view(),
        name='submit_caffeine'),
    url(r'^(?P<drink>(coffee|mate))/submit/(?P<username>[\w0-9@.+-_]+)'
        r'/(?P<token>\w+)/$',
        SubmitCaffeineOnTheRunView.as_view(),
        name='submit_caffeine_otr'),
    url(r'^action/confirm/(?P<code>\w+)/$',
        ConfirmActionView.as_view(),
        name='confirm_action'),
    url(r'^delete/(?P<pk>\d+)/$',
        DeleteCaffeineView.as_view(),
        name='delete_caffeine'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^profile/(?P<username>[\w0-9@.+-_]+)/$',
        PublicProfileView.as_view(),
        name='public'),
    url(r'^random-users$', random_users,
        name='random_users'),
]
