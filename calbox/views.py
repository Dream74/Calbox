from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib import auth
def index(request):
	return render_to_response('index.html', { 'user' : request.user })
