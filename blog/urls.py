from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^posts/(?P<id>\d+)/$', post_detail, name='post_detail'),
    url(r'^posts/new/$', new_post, name='new_post'),
    url(r'^posts/(?P<id>\d+)/edit$', edit_post, name='edit_post'),
]