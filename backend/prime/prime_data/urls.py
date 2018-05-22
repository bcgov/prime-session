'''
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'sessions/', views.SessionListView.as_view(), name='sessions'),
    url(r'session/<int:pk>', views.SessionDetailView.as_view(), name='sessionDetail'),
    url(r'newSession/', views.newSession, name='newSession'),
]
'''

from django.conf.urls import url, include

# generated views
from . import views
from .models import Session
# custom views

# Serializers define the API representation.
from rest_framework import routers, serializers, viewsets

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'browserHash', 'user', 'securityToken', 'retryToken')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'session', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'sessions/', views.SessionListView.as_view(), name='sessions'),
    url(r'session/<int:pk>', views.SessionDetailView.as_view(), name='sessionDetail'),
    url(r'newSession/', views.newSession, name='newSession'),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]