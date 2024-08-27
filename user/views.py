from django.shortcuts import render
from . import forms


def login(request):
    return render(request, 'user/login.html', {"form": forms.LoginForm()})


def new_post(request):
    return render(request, 'user/new_post.html', {'form': forms.NewPostForm()})
