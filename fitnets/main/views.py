from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from models import *

def index(request):
    if request.user.is_authenticated():
        return redirect(reverse('account.views.dashboard'))
    else:
        return redirect(reverse('registration.views.login'))