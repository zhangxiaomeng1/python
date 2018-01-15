from django.conf.urls import url

from sev import views

urlpatterns = [
    url(r'^$', views.index),


    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]
