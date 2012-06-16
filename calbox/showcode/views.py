from django.shortcuts import render_to_response
# cal-x HTML home index call code
def index(request):
  from django.core.context_processors import csrf
  c = {}
  c.update( csrf(request) )
  return render_to_response('showcode/index.html', c )
