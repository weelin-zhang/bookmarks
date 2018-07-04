from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout, login
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    # post views
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^logout/$', logout, {'next_page': reverse_lazy("account:login")}, name='logout'),
]
