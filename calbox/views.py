from django.shortcuts import render_to_response
# HTML Home index
def index(request):
	return render_to_response('index.html', { 'user' : request.user })
