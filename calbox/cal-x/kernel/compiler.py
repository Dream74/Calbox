from hashlib import md5
from compiler_c import core as core_c
from compiler_cc import core as core_cc
from compiler_java import core as core_java
def core(lang, user, code , question):
  if str.isdigit(  lang.encode('utf-8') ) : 
    lang_type = int( lang.encode('utf-8') ) 
    if lang_type == 11 : # c
			return core_c(mda( lang, user, question), user, code,  question)
    if lang_type == 1 : # c++
			return core_cc(mda( lang, user, question), user, code,  question)
    if lang_type == 10 : # JAVA
			return core_java(mda( lang, user, question), user, code,  question)
    return 'lang code no support'
  return 'lang is no integer'

def mda( lang, user, question ) :
	return md5( user.encode('utf-8')  + '_' + question.encode('utf-8')  ).hexdigest()
