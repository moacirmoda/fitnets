from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from models import *

@login_required
def index(request):
    return redirect(reverse('account.views.dashboard'))
    