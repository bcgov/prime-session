from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from primesession.views import index, health

from rest_framework import routers
from primesession import views


router = routers.DefaultRouter()
router.register(r'session', views.SessionViewSet)
router.register(r'token', views.TokenViewSet)


urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
