import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (RetrieveModelMixin, CreateModelMixin, ListModelMixin, RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin)
from primesession.serializer import Session,SessionSerializer


def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'primesession/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

class SessionViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin,DestroyModelMixin,UpdateModelMixin, GenericViewSet):

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = 'sessionid'

class TokenViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin,DestroyModelMixin,UpdateModelMixin, GenericViewSet):

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = 'token'

