from django.conf.urls import url
from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^users_courses', views.users_courses, name='users_courses'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^add_new$', views.add_new, name='add_new'),
    url(r'^$', views.index, name='index'),
]
