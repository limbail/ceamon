from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from ceamon.models import sapnode
import auth, json

@login_required(login_url='/login')
def main(request):
    c = {}
    c.update(csrf(request))

    if not request.user.is_authenticated():
        return redirect('auth.views.login_user',)

    danger = sapnode.objects.filter(status='danger').order_by('sid').values().distinct()
    danger_count=len(danger)

    warning = sapnode.objects.filter(status='warning').order_by('sid').values().distinct()
    warning_count=len(warning)

    instancias = sapnode.objects.filter().order_by('sid').values().distinct()
    instancias_count=len(instancias)

    return render_to_response('main/main.html',{
        #'danger':danger,
        #'danger_count':danger_count,
        #'warning':warning,
        #'warning_count':warning_count,
        #'instancias':instancias,
        #'instancias_count':instancias_count,

    },context_instance=RequestContext(request))

    #return render_to_response('main/main.html', context_instance=RequestContext(request))

