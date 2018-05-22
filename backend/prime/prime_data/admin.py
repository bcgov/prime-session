# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

# minimal registration of Session
from .models import Session
# admin.site.register(Session)



class SessionInline(admin.TabularInline):
    model = Session


class SessionAdmin(admin.ModelAdmin):
    """
    Administration object for Author models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('id', 'browserHash', 'user', 'securityToken', 'retryToken')
    fields = ['id', 'browserHash', 'user', 'securityToken', 'retryToken']
    inlines = [SessionInline]

