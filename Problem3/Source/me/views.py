from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse

def name(request):
	return render(request, 'homepage.html')

def home(request):
	name = request.POST['name']
	return render(request, 'index.html', {'user': name})

def aboutme(request):
	return render_to_response('aboutme.html')
