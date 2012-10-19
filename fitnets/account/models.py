from django.contrib.auth.models import User
from django.db.models import signals
from main.utils import gravatar
from django.db import models

class UserProfile(models.Model):

    user = models.ForeignKey(User, unique=True)

    def get_avatar(self):
        email = ""
        if self.user.email:
            email = self.user.email
        
        return gravatar(email)

def create_profile(sender, instance, created, **kwargs):
    user = instance
    try:
        profile = user.get_profile()
    except:
        profile = UserProfile(user=user)
        profile.save()

signals.post_save.connect(create_profile, sender=User, dispatch_uid="some.unique.string.id")