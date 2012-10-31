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

@login_required
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

@login_required
def show(request, id, slug):

    output = {}
    project = get_object_or_404(Project, id=id)
    comments = CommentProject.objects.filter(project=project).order_by('-id')[:10]

    comment_form = CommentProjectForm(initial={'project': id, 'creator': request.user.id})

    output['project'] = project
    output['comments'] = comments
    output['comment_form'] = comment_form

    return render_to_response("project/show.html", output, context_instance=RequestContext(request))

@login_required
def comment(request, project):

    output = {}
    project = get_object_or_404(Project, id=project)

    if request.POST:
        form = CommentProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('project.views.show', kwargs={'id': project.id, 'slug': project.slugify()}))
        else:
            return HttpResponse(form)