from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from welcome import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'session', views.SessionViewSet)
router.register(r'token', views.TokenViewSet)


urlpatterns = [

    url(r'^', include(router.urls)),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ] + urlpatterns
