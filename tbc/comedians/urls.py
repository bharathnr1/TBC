from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'comedians'

urlpatterns=[
    path(r'', views.view_comedians, name = 'view_comedians'),
    path(r'register_comedians/', views.register_comedians, name = 'register_comedians'),
    path(r'view_comedians/', views.view_comedians, name = 'view_comedians')
]
