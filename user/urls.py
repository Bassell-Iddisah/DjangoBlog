from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.login, name='login'),
    path('new_article/', views.new_post, name='new_post'),
]
