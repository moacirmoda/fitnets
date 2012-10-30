from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
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
