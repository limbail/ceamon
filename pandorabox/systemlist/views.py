from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from .forms import modify_form
from ceamon.models import sapnode
from django.core import serializers
from django.template.context_processors import csrf
from django.template import RequestContext

import auth

def systemlist(request):
    dic = {}
    dic.update(csrf(request))

    if not request.user.is_authenticated():
        return redirect('auth.views.login_user',)

    if request.method == 'POST':
        form = modify_form(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/systemlist/')

    else:
        form = modify_form()
        todo = list(sapnode.objects.all())

        data = serializers.serialize('json', todo)

        #return render(request, 'systemlist/systemlist.html', {'form': form, 'todo': todo,})
        return render_to_response('systemlist/systemlist.html',{'form': form, 'todo': todo,},context_instance=RequestContext(request))

