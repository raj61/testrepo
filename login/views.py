from django.shortcuts import render,render_to_response
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render_to_response('base.html')

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,'login.html',{"form":form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        user = User.objects.get(user_name=form.user_name)
        if form.password == user.password:
            return HttpResponseRedirect('/user')
        else:
            return HttpResponseRedirect('/error')
