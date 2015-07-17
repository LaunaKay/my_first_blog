from django.conf.urls import url
from . import views

urlpatterns =   [
                    url(r'^$', views.ninja, name='ninja'),
                    url(r'^(?P<color>\w+)/$', views.color, name='color'),
                ]