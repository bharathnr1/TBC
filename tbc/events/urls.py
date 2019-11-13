from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'events'

urlpatterns=[
    path('host_event/', views.host_event, name = 'host_event'),
    path('', views.view_events, name = 'view_events')
]
