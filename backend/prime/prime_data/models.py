# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Session(models.Model):
    """
    Model representing an instance of a session
    """
    browserHash = models.CharField(max_length=64, help_text="Hash of HTTP headers in session to prevent impersonization")
    user = models.CharField(max_length=128, help_text="User name")
    securityToken = models.CharField(max_length=256, help_text="Obtained Security Token")
    retryToken = models.CharField(max_length=256, help_text="Obtained Retry Token")
    
    def __str__(self):
        """
        return string about yourself
        """
        return 'sessionData:'.join(str(self.user)).join(':').join(str(self.pk))
    
    
     
    
    