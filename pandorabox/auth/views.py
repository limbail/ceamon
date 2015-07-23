from django.core.context_processors import csrf
from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def login_user(request):
    dic = {}
    dic.update(csrf(request))
    state = "Introduce tu usuario y password"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Login correcto!"
                return HttpResponseRedirect('/')
            else:
                state = "Cuenta inactiva, contacta con el administrador."
        else:
            state = "Tu usuario y/o password no son validos"

    return render_to_response('login/auth.html',{'state':state, 'username': username})

def logout_user(request):
    logout(request)
    return redirect('auth.views.login_user',)

