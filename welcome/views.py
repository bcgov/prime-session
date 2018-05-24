import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (RetrieveModelMixin, CreateModelMixin, ListModelMixin, RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin)
from welcome.serializer import Session,SessionSerializer



class SessionViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin,DestroyModelMixin,UpdateModelMixin, GenericViewSet):

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = 'sessionid'


class TokenViewSet(RetrieveModelMixin, CreateModelMixin, ListModelMixin,DestroyModelMixin,UpdateModelMixin, GenericViewSet):

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = 'token'
