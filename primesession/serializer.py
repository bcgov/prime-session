from rest_framework import serializers
from django.db import models

class Session(models.Model):
    sessionID = models.CharField(max_length=30,unique=True)
    token = models.CharField(max_length=30,unique=True)

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('sessionID', 'token')
