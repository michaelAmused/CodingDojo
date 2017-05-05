from django.conf.urls import url
from . import views

app_name = 'log_reg'
urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^user_reviews/(?P<id>\d+)$', views.user_reviews, name='user_reviews'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.index, name='index')
]
