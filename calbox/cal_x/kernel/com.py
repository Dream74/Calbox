import os
import subprocess
from conf import *
from cal_json import Compare_message, Error_message
from hashlib import md5
def core(lang, userm, code , question):
	update_code( m_lang, m_user, m_code, m_question )
	com_msn = complit( m_lang,  m_user, m_question )
	if com_msn == "" :
	 html = run( m_lang, m_user, m_question )
	else :
	 html = Compare_message( com_msn, 'Complit error')

def mda( lang, user, question ) :
	return 'b720ffbd02ba9498bc2d0e0f32ba821c'
	return md5( lang.encode('utf-8')  + '_' + user.encode('utf-8')  + '_' + quersion.encode('utf-8')  ).hexdigest()

def update_code( lang, user, code, question ):	
	fe = ''
	if str.isdigit(  lang.encode('utf-8') ) :
		lang_type = int( lang.encode('utf-8') ) 
		if lang_type == 11 : # c
			fe = FE_C
		if lang == 1 : # c++a
			fe = FE_CC
		if lang == 10 : # JAVA
			fe = FE_JAVA
	else :
		return 'Error update'
	code_dir = FILE_DIR + mda(lang, user, question) + '/'
	if not os.path.exists( code_dir ):
		os.makedirs( code_dir )
	
	code_file = open(  code_dir + FILE_NAME  + fe, 'w' )
	code_file.write( code )
	code_file.close()

def complit( lang, user, question ):
	fe =''
	com = ''
	if str.isdigit(  lang.encode('utf-8') ) :
		lang_type = int( lang.encode('utf-8') ) 
		if lang_type == 11 : # c
			fe = FE_C
			com = COM_C
		if lang_type == 1 : # c++
			fe = FE_CC
			com = COM_CC
		if lang_type == 10 : # JAVA
			fe = FE_JAVA
			com = COM_JAVA
		return 'No Support lang : %d' % ( lang )
	else :
		return 'lang is not Number'

	m_mda = mda(lang, user, question)
	code_file = FILE_DIR + m_mda + '/'+ FILE_NAME + fe
	if not os.path.exists( code_file ):
		print 'Code NO EXISTS'
	
	if not os.path.exists( BINARY_DIR + m_mda ):
		os.makedirs( BINARY_DIR + m_mda )
			
	pingPopen = subprocess.Popen(args=com + code_file +' -o '+  BINARY_DIR + FILE, shell=True, stderr=subprocess.PIPE)
	pingPopen.wait()
	return pingPopen.stderr.read()

def complit_c( user, question ):
	code_name = question+ '_'+ user+ FE_cc
	if not os.path.exists( FILE_DIR+code_name ):
		print 'Code NO EXISTS'
		
	binary_file = user	
	pingPopen = subprocess.Popen(args='g++ '+ FILE_DIR+ code_name+' -o '+BINARY_DIR+binary_file, shell=True, stderr=subprocess.PIPE)
	pingPopen.wait()
	return pingPopen.stderr.read()

def run( lang, user, question ):
	if str.isdigit( lang.encode('utf-8') ) :
		lang_type = int( lang.encode('utf-8') ) 
		if lang_type == 11 : # c
			FE = FE_C
		#if lang_type == 1 : # c++
		if lang_type == 10 : # JAVA
			FE = FE_JAVA
		return 'No Support lang : %d' % (lang)
	else :
		return 'lang is not Number'

def run_c( user, question ):
	p = subprocess.Popen( args=BINARY_DIR + user ,
	 										stdin = subprocess.PIPE,
											stdout = subprocess.PIPE,
											stderr = subprocess.PIPE,
											shell = True)    
	p.stdin.write('3\n')  
	p.stdin.write('4\n')  
	p.wait()
	run_msn = p.stderr.read()
	#os.remove( BINARY_DIR + user )
	if run_msn == '' :
		return Compare_message(p.stdout.read(), 'run_OK')
	else :		
		return Error_message(run_msn, 'run_error' )

def style_check( user, question ):
	return True

