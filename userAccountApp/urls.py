from django.conf.urls import url

from userAccountApp import views


urlpatterns = [
    url(r'^$', views.index, name="users"),
    url(r'^users/(?P<id>\d+)/$', views.user, name="user"),
]
