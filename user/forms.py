from django.forms import ModelForm
from . import models


class LoginForm(ModelForm):
    class Meta:
        model = models.User
        fields = ["email", "password"]


class NewPostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "body"]
