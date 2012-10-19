#! coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from wall.models import *
from wall.forms import *

@login_required
def profile(request, username):

    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).filter(parent=None)

    output = {
        'user': user,
        'posts': posts,
    }

    return render_to_response("profile.html", output, context_instance=RequestContext(request))

@login_required
def dashboard(request):

    forms = {
        'wall': PostForm(),
    }
    
    output = {
        'forms': forms,
    }

    return render_to_response("account/dashboard.html", output, context_instance=RequestContext(request))