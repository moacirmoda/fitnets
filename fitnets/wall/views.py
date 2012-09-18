#! coding: utf-8
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse
from models import *
from forms import *

def new(request, id):

    user = get_object_or_404(User, id=id)

    if request.POST:

        post = Post(user=user)
        post.creator = request.user
        post.updater = request.user
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect(reverse('account.views.profile', args=[request.user.username]) + "?action=wall")       
        else:
            print form.errors

def like(request, id):
    try:
        post = Post.objects.get(id=id)
        post.like = post.like + 1
        post.save()

        return HttpResponse(post.like)
    except:
        return HttpResponse(-1)

def unlike(request, id):
    try:
        post = Post.objects.get(id=id)
        post.non_like = post.non_like + 1
        print post.non_like
        post.save()

        return HttpResponse(post.non_like)
    except:
        return HttpResponse(-1)