#! coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from wall.models import *
from wall.forms import *
from friends.models import *

@login_required
def profile(request, username):

    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).filter(parent=None)

    friends = Friendship.objects.friends_of(user).values_list('id', flat=True)
    output = {
        'user': user,
        'posts': posts,
        'friends': friends,
    }

    return render_to_response("account/profile.html", output, context_instance=RequestContext(request))

@login_required
def dashboard(request):

    forms = {
        'wall': PostForm(),
    }

    user = get_object_or_404(User, username=request.user.username)
    friend_pending = FriendshipRequest.objects.filter(to_user=request.user).filter(accepted=False)
    friends = Friendship.objects.friends_of(user).values_list('id', flat=True)
    
    
    output = {
        'forms': forms,
        'friend_pending': friend_pending,
        'user': request.user,
        'friends': friends,
    }



    return render_to_response("account/dashboard.html", output, context_instance=RequestContext(request))