#! coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import RequestContext
from activity.models import *
from friends.models import *
from wall.models import *
from wall.forms import *
from forms import *

@login_required
def profile(request, username):

    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).filter(parent=None)[:10]
    projects = Project.objects.filter(creator=user).filter(finished=False).order_by('-id')[:6]
    friends = Friendship.objects.friends_of(user).values_list('id', flat=True)

    new_friends = []
    for friend in friends:
        friend = User.objects.get(id=friend)
        new_friends.append(friend)
        
    output = {
        'user': user,
        'posts': posts,
        'friends': new_friends,
        'projects': projects,
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
    projects = Project.objects.filter(creator=user).filter(finished=False)[:6]
    activities = Activity.objects.filter(creator__id__in=friends).order_by('-id')[:4]
    
    output = {
        'forms': forms,
        'friend_pending': friend_pending,
        'user': request.user,
        'friends': friends,
        'projects': projects,
        'activities': activities,
    }

    return render_to_response("account/dashboard.html", output, context_instance=RequestContext(request))

@login_required
def edit_profile(request):

    output = {}
    user = request.user
    profile = user.get_profile()
    form = EditUserForm(instance=profile)

    if request.POST:
        form = EditUserForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

    output['form'] = form
    output['user'] = user

    return render_to_response("account/edit_profile.html", output, context_instance=RequestContext(request))


