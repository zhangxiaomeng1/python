from django.conf.urls import url
from news import views


urlpatterns = [
    url(r'^$', views.index),

    url(r'^htmlEditor/$', views.htmlEditor),
    url(r'^htmlEditorHandle/$', views.htmlEditorHandle),
]