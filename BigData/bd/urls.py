from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^apply', views.apply, name='apply'),
	url(r'^contact', views.contact, name='contact'),
	url(r'^college', views.college, name='college'),
	url(r'^agenda', views.agenda, name='agenda'),
	url(r'^$', views.index, name='index'),
	]