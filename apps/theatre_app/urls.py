from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^profile$', views.profile),
    url(r'^login$', views.login),
    url(r'^register$', views.register),

]
