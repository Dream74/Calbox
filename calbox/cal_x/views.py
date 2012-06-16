from django.http import HttpResponse
from calbox.cal_x.question.models import Question_Code
# cal-x HTML home index call code
def code(request, homework ):
  # if user non-login, you can reload to login HTML
  #if not request.user.is_authenticated():
  #  from django.http import HttpResponseRedirect
  #  return HttpResponseRedirect("/accounts/login/")

  from django.core.context_processors import csrf
  c = {}
  c.update( csrf(request) )
  q_list = []
  try :
    if request.user.is_authenticated() and homework  :
      q_list =  Question_Code.objects.get_usr_question( request.user ) 
    elif not homework :
      q_list =  Question_Code.objects.get_all_question()
  except Question_Code.DoesNotExist:
      q_list = []

  if request.user.is_authenticated() :
    from calbox.cal_x.usr_code.models import Code_Done
    qlist = []
    ulist = Code_Done.objects.get_my_code( m_usr = request.user )
    for ql in q_list :
      qlist += [{ 'id' : ql.id, 'title' : ql.title, 'done' : False } ]
      for i in range( len(ulist) ) :
        if ulist[i].question == ql:
          qlist[-1]['done'] = True
          break
  else :
    qlist = q_list 
  c.update( { 'user' : request.user, 'q_list' : qlist } )
  from django.shortcuts import render_to_response
  return render_to_response('cal_x/index.html', c)

import json
# user steps : update_post_code -> core ( run )
# input : com_run(bool) : core operate run code
def update_post_code( request, com_run ):
  # if user non-login, prohibit user update code 
  #if not request.user.is_authenticated():
  #from django.http import Http404
  #raise Http404('plase login user')

  html = "NO POST"	
  if request.method == 'POST' :
    # user code lang : C(11), C++(1), JAVA(10)
    m_lang = request.POST.get('lang', '')
    # user code text
    m_code = request.POST.get('code', '' )
    # user select question index
    m_question = request.POST.get('question', '')

    m_supermode = False
    if request.user.is_authenticated():
      m_user = request.user.username

      # user login state, code into database( Code ), next login push down
      if com_run :
        if request.user.is_superuser and request.POST.get('supermode', '') == "true" :
          m_supermode = True
      else :
        from calbox.cal_x.usr_code.models import Code
        Code.objects.insert_code( request.user, int(m_lang), m_code.encode('utf8'), int(m_question) )
        return HttpResponse("")

    else :
      import datetime
      m_user = datetime.datetime.now().isoformat()

    if com_run and m_user != '' and m_question != '' and m_lang != '' :
      from kernel.kernel import core
      from kernel.conf import conf
      html = core( m_lang, m_user, m_code, m_question, m_supermode )
      # if run code success all I/O test, Code into DabaBase( Code_Done )
      if not m_supermode and request.user.is_authenticated() and json.loads( html )['type'].encode('utf8') == conf.RUN_OK:         
        from calbox.cal_x.usr_code.models import Code_Done
        Code_Done.objects.insert_code( request.user, int(m_lang), m_code.encode('utf8'), int(m_question) )
    else :
      html = 'have been space'

  return HttpResponse(html)

# return question doc 
# input : q_id : question index.
def question_doc(request, q_id ):
  return HttpResponse( Question_Code.objects.get_question_doc( q_id )  )

# return user last code record
def mycode( request ):
  if not request.user.is_authenticated():
    return HttpResponse( json.dumps({"code": "" , "readline": ''}, ensure_ascii = False) )
 

  if request.method == 'POST' :
    m_user = request.user.username
    # user code lang : C(11), C++(1), JAVA(10)
    m_lang = request.POST.get('lang', '')
    # user select question index
    m_question = request.POST.get('question', '')

    if m_question != '' and m_lang != '' :
      #return HttpResponse( json.dumps({"code": "" , "readline": ''}, sort_keys=True, indent=4, ensure_ascii = False) )
      # return json format( code: last recored code, readline : textarea readline number )
      from calbox.cal_x.usr_code.models import Code
      return HttpResponse( json.dumps({"code": Code.objects.getcode_text( request.user, m_lang, m_question ) , "readline": ''}, ensure_ascii = False) )
      #return HttpResponse( json.dumps({"code": get_code( m_lang, m_user, m_question ) , "readline": '0,2,5,6,'}, sort_keys=True, indent=4, ensure_ascii = False) )
  return HttpResponse( json.dumps({"code": "" , "readline": ''}, ensure_ascii = False) )

# return example code with lang
def example_code( request, lang_id ):
  from example.example import example_hello
  return HttpResponse( example_hello( lang_id )  )

