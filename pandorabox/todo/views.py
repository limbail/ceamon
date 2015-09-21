from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from ceamon.models import sapnode
from itertools import chain
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from .models import Notification

def w_problem_View(request):

    if not request.user.is_authenticated():
        return redirect('auth.views.login_user',)

    danger = sapnode.objects.filter(status='danger').order_by('sid').values().distinct()
    danger_count=len(danger)

    warning = sapnode.objects.filter(status='warning').order_by('sid').values().distinct()
    warning_count=len(warning)

    instancias = sapnode.objects.filter().order_by('sid').values().distinct()
    instancias_count=len(instancias)

    return render_to_response('todo/index.html',{
        'danger':danger,
        'danger_count':danger_count,
        'warning':warning,
        'warning_count':warning_count,
        'instancias':instancias,
        'instancias_count':instancias_count,


},context_instance=RequestContext(request))

class Notifications(ListView):
    model = Notification
    template_name = 'todo/index.html'

    def get_queryset(self):
        return self.model.objects.order_by('-pk')[:5]

from django import template
register = template.Library()

@register.assignment_tag
def query(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
          {% query books author=author as mybooks %}
          {% for book in mybooks %}
            ...
          {% endfor %}
    """
    return qs.filter(**kwargs)
