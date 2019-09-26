from django.shortcuts import redirect
from django.contrib import messages
from .models import *


def register(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if len(errors) > 0:
            for error in errors.values():
                messages.error(request, error)
        else:
            User.objects.add_user(request.POST)
            user = User.objects.get(username=request.POST['username'])
            request.session['username'] = user.username
            request.session['id'] = user.id
    return redirect('/')


def login(request):
    if request.method == "POST":
        if User.objects.login(request.POST):
            user = User.objects.get(username=request.POST['username'])
            request.session['username'] = user.username
            request.session['id'] = user.id
        else:
            messages.info(request, "Login Unsuccessful")
    return redirect('/')


def logout(request):
    if 'id' in request.session:
        del request.session['username']
        del request.session['id']
    return redirect('/')
