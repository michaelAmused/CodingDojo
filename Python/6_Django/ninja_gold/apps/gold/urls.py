from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^process_money/?([a-zA-Z0-9+-_]+)$', views.process_money),
    url(r'^$', views.index),
]
