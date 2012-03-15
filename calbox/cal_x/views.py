from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from calbox.cal_x.question.models import Question_Code
def code(request):
	#if not request.user.is_authenticated():
	#	return HttpResponseRedirect("/accounts/login/")
	c = {}
	c.update( csrf(request) )
	c.update( { 'user' : request.user, 'q_list' : Question_Code.objects.get_all_question()  })
	#c.update( { 'user' : request.user, 'q_list' : Question_Code.objects.get_usr_question( request.user)  })
	return render_to_response('cal_x/index.html', c)

from kernel.compiler import core, mda
from calbox.cal_x.usr_code.models import Code
import json
import datetime
def update_post_code( request, com_run ):
	#if not request.user.is_authenticated():
	#	raise Http404('plase login user')

	html = "NO POST"	
	if request.method == 'POST' :
		if request.user.is_authenticated():
			m_user = request.user.username
		else :
			m_user = datetime.datetime.now().isoformat()
		m_lang = request.POST.get('lang', '')
		m_code = request.POST.get('code', '' )
		m_question = request.POST.get('question', '')
		#html = 'lang :%s<br>user :%s <br>code :%s <br>qustion :%s' % ( m_lang, m_user, m_code, m_question )
		#return HttpResponse( html )
		if m_user != '' and m_question != '' and m_lang != '' :
			#html = "update"	
			html = core( m_lang, m_user, m_code, m_question, com_run ) 
			if com_run and json.loads( html )['type'].encode('utf8') == 'OK': 
				Code.objects.insert_code( request.user, int(m_lang), m_code.encode('utf8'), int(m_question) )
		else :
			html = 'have been space'

		if not request.user.is_authenticated(): 
			from shutil import rmtree
			rmtree( '/home/cal/ramdisk/code/' + mda( m_lang, m_user, m_question)  )
	return HttpResponse(html)

def question_doc(request, q_id ):
	return HttpResponse( Question_Code.objects.get_question_doc( q_id )  )

from kernel.compiler import get_code
def mycode( request ):
	if not request.user.is_authenticated():
		return HttpResponse( json.dumps({"code": "" , "readline": ''}, sort_keys=True, indent=4, ensure_ascii = False) )

	if request.method == 'POST' :
		m_user = request.user.username
		m_lang = request.POST.get('lang', '')
		m_question = request.POST.get('question', '')
		#html = 'lang :%s<br>user :%s <br>qustion :%s' % ( m_lang, m_user, m_question )
		#return HttpResponse( html )
		if m_user != '' and m_question != '' and m_lang != '' :
			return HttpResponse( json.dumps({"code": get_code( m_lang, m_user, m_question ) , "readline": ''}, sort_keys=True, indent=4, ensure_ascii = False) )
			#return HttpResponse( json.dumps({"code": get_code( m_lang, m_user, m_question ) , "readline": '0,2,5,6,'}, sort_keys=True, indent=4, ensure_ascii = False) )
	return HttpResponse( json.dumps({"code": "" , "readline": ''}, sort_keys=True, indent=4, ensure_ascii = False) )

	
from example.example import example_hello
def example_code( request, lang_id ):
	return HttpResponse( example_hello( lang_id )  )

