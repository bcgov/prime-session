# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from .models import Session
from django.contrib.admin.sites import site

def index(request):
    """
    View function for home page of site
    """
    # generate counts of the main objects)
    num_sessions = Session.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context={'num_sessions':num_sessions},
    )
    
from django.views import generic

class SessionListView(generic.ListView):
    model = Session
    paginate_by = 10
    
class SessionDetailView(generic.DetailView):
    model = Session
    
    
# permissions for create
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def newSession(request):
    """
    creating a new sessionInstance
    """
    if request.method == 'POST' or request.method == 'GET':
        # get the HTTP_USER_AGENT
        http_host = request.get_host()
        http_user_agent = request.META['HTTP_USER_AGENT']
        remote_address = request.META['REMOTE_ADDR']
        username = ''
        if request.user.is_authenticated():
            username = request.user.username
        browserHash = hash(http_host.join(':').join(http_user_agent).join(':').join(remote_address).join(':').join(username))
        sessionInstance = Session(browserHash=browserHash, user=username, securityToken='', retryToken='')
        sessionInstance.save()
        response = HttpResponse(sessionInstance.id)
        return response
    
    

