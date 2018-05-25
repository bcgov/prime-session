import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (RetrieveModelMixin, CreateModelMixin, ListModelMixin, RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin)
from prime.serializer import Session,SessionSerializer
from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'prime/index.html', {
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
