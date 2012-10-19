from django import template
from friends.models import *
register = template.Library()

@register.filter
def is_friend(user, user2):
    return bool(Friendship.objects.are_friends(user, user2))

@register.filter
def is_friend_pending(user, user2):
    return bool(Friendship.objects.is_pending(user1=user, user2=user2))