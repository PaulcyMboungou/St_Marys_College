from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('bd/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def agenda(request):
	template = loader.get_template('bd/agenda.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def college(request):
	template = loader.get_template('bd/college.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def contact(request):
	template = loader.get_template('bd/contact.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def apply(request):
	template = loader.get_template('bd/apply.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

