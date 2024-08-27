from django.shortcuts import render
from . import forms


def login(request):
    form = forms.LoginForm()
    return render(request, 'user/login.html', {"form": form})
