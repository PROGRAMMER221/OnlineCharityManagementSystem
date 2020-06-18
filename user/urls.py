from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="user/logout.html"), name='logout'),
]
