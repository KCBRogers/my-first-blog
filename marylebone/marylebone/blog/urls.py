from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^democracy$', views.democracy, name='democracy'),
    url(r'^events$', views.events, name='events'),
]

     
