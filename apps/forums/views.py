from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    user = None
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
    contents = {
        "posts": Post.objects.all().order_by('-created_at'),
        "user": user
    }
    return render(request, 'forums/index.html', contents)


def post(request, post_id):
    contents = {
        "post": Post.objects.get(id=post_id)
    }
    return render(request, 'forums/post.html', contents)


def newpost(request):
    author = User.objects.get(id=request.session['id'])
    Post.objects.create_post(request.POST, author)
    return redirect('/')


def upvote(request, post_id):
    if 'id' in request.session:
        Post.objects.vote(request.session['id'], 1, post_id)
    else:
        messages.error(request, "You must be logged in to vote.")
    return redirect('/')


def downvote(request, post_id):
    if 'id' in request.session:
        Post.objects.vote(request.session['id'], -1, post_id)
    else:
        messages.error(request, "You must be logged in to vote.")
    return redirect('/')
