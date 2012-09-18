from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

def dashboard(request):
    return render_to_response("dashboard.html", {}, context_instance=RequestContext(request))