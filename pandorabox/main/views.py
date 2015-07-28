from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
import auth, json

@login_required(login_url='/login')
def main(request):
    c = {}
    c.update(csrf(request))

    return render_to_response('main/main.html', context_instance=RequestContext(request))

