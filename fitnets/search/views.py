from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.db.models import Q
from project.models import *

@login_required
def search(request):

    output = {}
    
    try:    
        q = request.GET.get('q')
        itens = request.GET.getlist('itens[]')
    except:
        q = False
        itens = False

    projects = None
    users = None
    total = 0

    if q and itens:
        
        print itens
        if 'projeto' in itens:
            projects = Project.objects.filter(objective__icontains=q)[:10]
            print 'lelelee'
            total += len(projects)


        if 'user' in itens:
            print 'lelelele'
            users = User.objects.filter(Q(username__icontains=q) | Q(first_name__icontains=q))[:10]
            total += len(users)


    output['projects'] = projects
    output['users'] = users
    output['total'] = total
    output['itens'] = itens

    return render_to_response("search/search.html", output, context_instance=RequestContext(request))
