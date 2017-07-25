from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^remove/(\d+)$', views.remove),
    url(r'^delete/(\d+)$', views.delete),
    url(r'^add_new$', views.add_new),
    url(r'^$', views.index),
]
