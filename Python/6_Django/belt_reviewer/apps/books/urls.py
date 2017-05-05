from django.conf.urls import url
from . import views

app_name = 'books'
urlpatterns = [
    url(r'^destroy_review/(?P<id>\d+)$', views.destroy_review, name='destroy_review'),
    url(r'^add_review/(?P<id>\d+)$', views.add_review, name='add_review'),
    url(r'^show_book/(?P<id>\d+)$', views.show_book, name='show_book'),
    url(r'^add_book/', views.add_book, name='add_book'),
    url(r'^create/(?P<id>\d+)$', views.create, name='create'),
    url(r'^$', views.index, name='index')
]
