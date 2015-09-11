from django.core.context_processors import csrf
from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from .models import *
from .forms import LockerForm

@csrf_protect
def LockerView(request):
    dic = {}
    dic.update(csrf(request))

    SALT_SIZE = 8

    if not request.user.is_authenticated():
        return redirect('auth.views.login_user',)

    if request.method == 'POST':
        form = LockerForm(request.POST)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.hostname = "HOSTNAME"
            ins.sid = 'SID'
            ins.save()
            return HttpResponseRedirect(reverse('locker', ))
    else:
        form = LockerForm()
    todo = locker.objects.all()

    return render_to_response('locker/locker.html', {
                             'todo':todo,
                             'form':form,
                             }, context_instance=RequestContext(request),)

