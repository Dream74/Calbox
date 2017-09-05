#from compiler_c import core as core_c, update_code as update_c, get_code as get_code_c
#from compiler_cc import core as core_cc, update_code as update_cc, get_code as get_code_cc
#from compiler_java import core as core_java, update_code as update_java, get_code as get_code_java
from compiler import compiler as c_compiler
from compiler_cc import compiler_cc as cc_compiler
from compiler_java import compiler_java as java_compiler
# cal-x core 
# input : lang :( supple C, C++, JAVA ), user : user name, code : user input code, question : question index, com_run(bool) : touch run code
# return : if com_run is True : run message
def core(lang, user = None, code = None, question = None):
  if str.isdigit(  lang.encode('utf-8') ) : 
    lang_type = int( lang.encode('utf-8') ) 
    if lang_type == 11 : # c
      return c_compiler( user, code, question )
    elif lang_type == 1 : # c++
      return cc_compiler( user, code, question )
    elif lang_type == 10 : # JAVA
      return java_compiler( user, code, question )
    return 'lang code no support'
  return 'lang is no integer'

# return user last code record 
def get_code(lang, user, question ):
  from calbox.cal_x.usr_code.models import Code
  try :
    return Code.objects.getcode_text( usr, lang, question ) 
  except Code.DoesNotExist:
    return '' 

