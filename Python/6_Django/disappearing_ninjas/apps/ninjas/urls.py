from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ninjas/?([a-zA-Z0-9+-_]+)$', views.ninjas),
    url(r'^$', views.index),
]
