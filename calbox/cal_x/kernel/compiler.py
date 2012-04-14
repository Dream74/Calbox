from compiler_c import core as core_c, update_code as update_c, get_code as get_code_c
from compiler_cc import core as core_cc, update_code as update_cc, get_code as get_code_cc
from compiler_java import core as core_java, update_code as update_java, get_code as get_code_java
# cal-x core 
# input : lang :( supple C, C++, JAVA ), user : user name, code : user input code, question : question index, com_run(bool) : touch run code
# return : if com_run is True : run message
def core(lang, user, code , question, com_run ):
  if str.isdigit(  lang.encode('utf-8') ) : 
    lang_type = int( lang.encode('utf-8') ) 
    if com_run :
      if lang_type == 11 : # c
	  		return core_c(mda( lang, user, question), user, code,  question)
      if lang_type == 1 : # c++
	  		return core_cc(mda( lang, user, question), user, code,  question)
      if lang_type == 10 : # JAVA
	  		return core_java(mda( lang, user, question), user, code,  question)
    else :
      if lang_type == 11 : # c
  			return update_c(mda( lang, user, question), code )
      if lang_type == 1 : # c++
  			return update_cc(mda( lang, user, question), code )
      if lang_type == 10 : # JAVA
  			return update_java(mda( lang, user, question), code )
    return 'lang code no support'
  return 'lang is no integer'

# return user last code record 
def get_code(lang, user, question ):
  if str.isdigit(  lang.encode('utf-8') ) : 
    lang_type = int( lang.encode('utf-8') ) 
    code = ""
    # get code from temp file
    if lang_type == 11 : # c
      code = get_code_c(mda( lang, user, question))
    elif lang_type == 1 : # c++
      code = get_code_cc(mda( lang, user, question))
    elif lang_type == 10 : # JAVA
      code = get_code_java(mda( lang, user, question))
    else :
      return 'lang code no support'
    
    # if temp file code is empty, try from databast get usr code
    if code == "" :
      from calbox.cal_x.usr_code.models import Code
      return Code.objects.getcode_text( usr, lang, question ) 
    else :
      return code 
  return 'lang is no integer'

# cal-x ( lang, user, question) to dir path
def mda( lang, user, question ) :
  return user.encode('utf-8')  + '_' + question.encode('utf-8')
  from hashlib import md5
  return md5( user.encode('utf-8')  + '_' + question.encode('utf-8')  ).hexdigest()
