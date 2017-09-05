from django.http import HttpResponse
from django.shortcuts import render_to_response
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

def get_input( request ) :
  if request.method == 'GET' :
    _qid = request.GET.get('q_id', '')
    if _qid != '':
      from calbox.cal_x.question.models import Question_IO
      import json
      q_list = Question_IO.objects.get_question_io( int(_qid) ).filter(occult=False)
      i_list = []
      for l in q_list :
        i_list += [ { "input_list" : l.input_text.encode('utf-8') } ] 
      return HttpResponse( json.dumps( i_list, ensure_ascii = False ) )

  return HttpResponse('')
