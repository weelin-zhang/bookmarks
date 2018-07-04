from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
]
