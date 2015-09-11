from django.core.context_processors import csrf
from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from ceamon.models import sapnode, StatusModel
from operator import attrgetter
from itertools import chain
from .forms import OverviewForm
from django.core.urlresolvers import reverse

def overview(request):
    dic = {}
    dic.update(csrf(request))

    if not request.user.is_authenticated():
        return redirect('auth.views.login_user',)

    if request.method == 'POST':
        form = OverviewForm(request.POST)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.comment = "HOSTNAME"
            ins.save()
            return HttpResponseRedirect(reverse('overview', ))

    else:
        form = OverviewForm()

    todo = StatusModel.objects.all().order_by('status').values().distinct()
    return render_to_response('overview/overview.html',{'todo':todo, 'form':form,},context_instance=RequestContext(request))
