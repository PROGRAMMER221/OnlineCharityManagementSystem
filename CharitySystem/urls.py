from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.header, name="header"),
    url(r'^self/$', views.about, name="about"),
    url(r'^get_verified/$', views.ngo, name="ngo"),
    url(r'^not_verified/$', views.not_verified, name="not_verified"),
    url(r'^admin_verify/$', views.verify_from_admin, name="verification_from_admin"),
    url(r'^verified_as_true/(?P<pk>\d+)/$',views.Verification_Status_True, name="verified_as_true"),
    url(r'^verified_as_false/(?P<pk>\d+)/$',views.Verification_Status_False, name="verified_as_false"),
    url(r'^mail_Y/$', views.mail_Y, name="mail_of_acceptance"),
    url(r'^mail_N/$', views.mail_N, name="mail_of_rejectance"),
    url(r'^post_request/$', views.post_request, name="post_request"),
    url(r'^fund_request/$', views.donation,name="fund request"),
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^charge/$', views.charge, name="charge"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)