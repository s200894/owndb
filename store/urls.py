﻿from django.conf.urls import patterns, include, url
from store.views import ProjectList
from store.views import FormList
from store.views import FormInstanceList
from store.views import FormInstanceDetail

urlpatterns = patterns(
	'',
	url(r'^/(?P<page>[0-9]+)/$', ProjectList.as_view(), name='project-list'),
	url(r'^/?$', ProjectList.as_view(), name='project-list'),
	url(r'^(?P<project>[\w\-\_]+)/(?P<page>[0-9]+)/$', FormList.as_view(), name='form-list'),
	url(r'^(?P<project>[\w\-\_]+)$', FormList.as_view(), name='form-list'),
	url(r'^(?P<project>[\w\-\_]+)/(?P<form>[\w\-\_]+)/(?P<page>[0-9]+)/$', FormInstanceList.as_view(), name='forminstance-list'),
	url(r'^(?P<project>[\w\-\_]+)/(?P<form>[\w\-\_]+)$', FormInstanceList.as_view(), name='forminstance-list'),
	url(r'^(?P<project>[\w\-\_]+)/(?P<form>[\w\-\_]+)/(?P<forminstance>[\w\-\_]+)/(?P<page>[0-9]+)/$', FormInstanceDetail.as_view(), name='forminstance-detail'),
	url(r'^(?P<project>[\w\-\_]+)/(?P<form>[\w\-\_]+)/(?P<forminstance>[\w\-\_]+)$', FormInstanceDetail.as_view(), name='forminstance-detail'),
	url(r'^add_form', 'store.views.add_form', name='add_form'),
    )