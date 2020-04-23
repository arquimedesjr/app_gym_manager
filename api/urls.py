from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import api


urlpatterns = (
    # api
    url(r'^(?P<pk>[0-9]+)/(?P<param>[\w-]+)', api, name='api'),
)
