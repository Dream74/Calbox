from django.http import HttpResponse
# cal-x HTML home index call code
def index(request):
  from django.shortcuts import render_to_response
  #return HttpResponse('close showcode')
  return render_to_response('showcode/index.html')

