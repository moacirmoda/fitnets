from django.db.models import signals as SIGNALS
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from main.utils import gravatar
from datetime import datetime as dt
from django.db import models
from friends.models import *
from decimal import Decimal
from project.models import *
from datetime import date

class UserProfile(models.Model):

    user = models.ForeignKey(User, unique=True)
    created = models.DateTimeField("data de registro", default=dt.now(), editable=False)
    
    born = models.DateField("nascimento", blank=True, null=True)
    height = models.IntegerField("altura", blank=True, null=True)
    weight = models.IntegerField("peso", blank=True, null=True)
    facebook = models.URLField("facebook", blank=True, null=True)
    bio = models.TextField("sobre", blank=True, null=True)

    def permalink(self):
        return reverse('account.views.profile', kwargs={'username': self.user})

    def get_avatar(self, size=220):
        email = ""
        if self.user.email:
            email = self.user.email        
        return gravatar(email, width=size)

    def get_medium_avatar(self):
        return self.get_avatar(size=120)

    def get_mini_avatar(self):
        return self.get_avatar(size=66)

    def get_94_avatar(self):
        return self.get_avatar(size=94)
        
    def get_height_in_meters(self):
        return Decimal(self.height)/Decimal(100)
    
    def get_weight_in_kg(self):
        return unicode("%s m" % Decimal(self.weight)/Decimal(100))

    def get_name(self):
        if self.user.first_name:
            return unicode(self.user.first_name)
        return unicode(self.user)
    
    def get_full_name(self):
        if self.user.first_name:
            return unicode("%s %s" % (self.user.first_name, self.user.last_name))
        return unicode(self.user)

    def get_open_projects(self):
        projects = Project.objects.filter(creator=self.user).filter(finished=False)
        if projects:
            return len(projects)
        return 0

    def get_closed_projects(self):
        projects = Project.objects.filter(creator=self.user).filter(finished=True)
        if projects:
            return len(projects)
        return 0

def create_profile(sender, instance, created, **kwargs):
    user = instance
    try:
        profile = user.get_profile()
    except:
        profile = UserProfile(user=user)
        profile.save()
SIGNALS.post_save.connect(create_profile, sender=User, dispatch_uid="some.unique.string.id")

def create_friendship(sender, instance, created, **kwargs):
    user = instance
    try:
        friendship = Friendship.objects.get(user=user)
    except:
        friendship = Friendship(user=user)
        friendship.save()
SIGNALS.post_save.connect(create_friendship, sender=User, dispatch_uid="some.unique.string.id2")

