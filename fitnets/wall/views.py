#! coding: utf-8
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse
from models import *
from forms import *

@login_required
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

@login_required
def like(request, id):
    try:
        post = Post.objects.get(id=id)
        post.like = post.like + 1
        post.save()

        return HttpResponse(post.like)
    except:
        return HttpResponse(-1)

@login_required
def unlike(request, id):
    try:
        post = Post.objects.get(id=id)
        post.non_like = post.non_like + 1
        post.save()

        return HttpResponse(post.non_like)
    except:
        return HttpResponse(-1)

@login_required
def more(request, user, from_):

    output = {}
    user = get_object_or_404(User, id=user)
    posts = Post.objects.filter(user=user).filter(parent=None)[from_:10]

    if not posts:
        return HttpResponse("-1")

    output['posts'] = posts

    return render_to_response("wall/block-wall.html", output, context_instance=RequestContext(request))


