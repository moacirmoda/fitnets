from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from models import *
from forms import *

@login_required
def new(request):

    output = {}
    form = ProjectForm()

    if request.POST:
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print form.errors

    output['form'] = form

    return render_to_response("project/new.html", output, context_instance=RequestContext(request))

def list(request, username, type=None):

    output = {}
    user = User.objects.get(username=username)
    finished = False
    if type == 'closed':
        finished = True

    if type == "all":
        projects = Project.objects.filter(creator=user)[:10]
    else:
        projects = Project.objects.filter(creator=user).filter(finished=finished)[:10]

    output['user'] = user
    output['projects'] = projects
    output['finished'] = finished
    output['type'] = type

    return render_to_response("project/list.html", output, context_instance=RequestContext(request))

