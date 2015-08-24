from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from ceamon.models import sapnode
from main.forms import LockerForm
import auth, json

@login_required(login_url='/login')
def main(request):
    status = "TEST"
    c = {}
    c.update(csrf(request))

    if not request.user.is_authenticated():
        return redirect('auth.views.login_user',)

    if request.method == 'POST':
        form = LockerForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            url = form.cleaned_data['url']
            notes = form.cleaned_data['notes']
            form.save(commit=True)
            status = "CORRECTO"

            if request.is_ajax():
                return render(request, 'main/main.html')

        else:
            print form.errors
            status = "ERROR"
    else:
        form = LockerForm()

    return render_to_response('main/main.html',{
        'form':form,
        'status':status
    },context_instance=RequestContext(request))

    #return render_to_response('main/main.html', context_instance=RequestContext(request))

