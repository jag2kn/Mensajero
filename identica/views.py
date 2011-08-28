# Create your views here.
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    backends = grouped_backends()
    return render_to_response('home.html', {'version': version,
                                            'backends': backends},

