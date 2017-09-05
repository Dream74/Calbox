from django.http import HttpResponse
from django.shortcuts import render_to_response
# cal-x HTML home index call code
def index(request):
  from django.core.context_processors import csrf
  c = {}
  c.update( csrf(request) )
  return render_to_response('testcode/index.html', c )

# user steps : update_post_code -> core ( run )
# input : com_run(bool) : core operate run code
def update_post_code( request ):
  html = "NO POST"  
  if request.method == 'POST' :
    # user code lang : C(11), C++(1), JAVA(10)
    m_lang = request.POST.get('lang', '') 
    # user code text
    m_code = request.POST.get('code', '' )
    # user code input
    m_Cin = request.POST.get('Cin', '' )
    
    if m_lang != '' and m_code != '':
      from calbox.cal_x.kernel.kernel import core
      from calbox.cal_x.kernel.conf import conf
      com = core( m_lang, None, m_code )
      com.kernel( IOlist=[{"input": m_Cin, "output": ""}])
      import json
      import re
      html = json.dumps( { "output" : com.getRout(), "compiler_warn" : re.compile(r'.+[\\\/]').sub('', com.getComMes()) }, ensure_ascii = False )
    else :
      html = 'have been space'

  return HttpResponse(html)

