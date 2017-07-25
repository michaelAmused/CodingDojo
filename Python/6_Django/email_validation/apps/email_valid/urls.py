from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.create),
    url(r'^emails$', views.emails),
    url(r'^$', views.index),
]
