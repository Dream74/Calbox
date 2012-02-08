from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from kernel.compiler import core
from example.example import example_hello
def code(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/accounts/login/")
	c = {}
	c.update( csrf(request) )
	
	example_lang = request.GET.get('example_lang', '' )
	c.update( { 'user' : request.user, 'code' : example_hello( example_lang )  })
	return render_to_response('cal_x/index.html', c)

from calbox.cal_x.usr_code.dbapi import insert_code
import json
def update_post_code(request):
	if not request.user.is_authenticated():
		raise Http404('plase login user')

	html = "NO POST"	
	if request.method == 'POST' :
		m_user = request.user.username
		m_lang = request.POST.get('lang', '')
		m_code = request.POST.get('code', '' )
		m_question = request.POST.get('question', '')
		html = 'lang :%s<br>user :%s <br>code :%s <br>qustion :%s' % ( m_lang, m_user, m_code, m_question )
		#return HttpResponse( html )
		if m_user != '' and m_code != '' and m_question != '' and m_lang :
			#html = "update"	
			html = core( m_lang, m_user, m_code, m_question ) 
			if json.loads( html )['type'].encode('utf8') == 'OK': 
				insert_code( request.user, int(m_lang), m_code.encode('utf8'), int(m_question) )
		else :
			html = 'have been space'
	return HttpResponse(html)

from calbox.cal_x.question.dbapi import get_question_doc
def question_doc(request, q_id ):
	return HttpResponse( get_question_doc( q_id )  )
	

