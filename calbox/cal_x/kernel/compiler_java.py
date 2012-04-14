# -*- coding: utf-8 -*-
import os
import subprocess
from conf import *
from re_message import json_message
# cal-x core update-> complite-> style-> run (check I/O)
# input : mda: temp path, user : user name, code : user code, question :user select question
def core( mda, user, code, question):
  # prohibit code more big
  if len( code ) > CODE_FILE :
    return json_message( CODE_SIZE_LIMIT, COM_ERR )

  # update code to temp
  update_code( mda, code )

  # complite code from temp
  com_msn = complit( mda )
  if com_msn == "" :
    # styple code
    style_msn = style_check( code )
    if style_msn == "" :
      # run code check I/O
			return run( mda, question )
    else :
     return json_message( style_msn, STYPLE)
  else :
   return json_message( com_msn, COM_ERR)

# return user code from temp
def get_code( mda ):
  code_dir = FILE_DIR + mda + '/'
  if not os.path.exists( code_dir ) or not os.path.exists( code_dir + FILE_NAME  + FE_JAVA ):
    return ""

  code_file = open(  code_dir + FILE_NAME  + FE_JAVA , 'r' )
  return code_file.read()

# update code to temp
def update_code( mda, code ):  
  code_dir = FILE_DIR + mda + '/' 
  if not os.path.exists( code_dir ):
    os.makedirs( code_dir )
  
  code_file = open(  code_dir + FILE_NAME  + FE_JAVA , 'w' )
  code_file.write( code.encode('utf8') )
  return code_file.close()

def complit( mda ):
  file_code = FILE_DIR + mda + '/' +FILE_NAME + FE_JAVA 
  if not os.path.exists( file_code ) :
    return 'Code NO EXISTS'

  binary_dir =  BINARY_DIR + mda + '/'
  if not os.path.exists( binary_dir ) :
    os.makedirs( binary_dir )
    
  pingPopen = subprocess.Popen(args='javac '+ file_code + ' -d '+ binary_dir , shell=True, stderr=subprocess.PIPE)
  pingPopen.wait()
  return pingPopen.stderr.read()

# run all I/O, and check
def run( mda, m_question ):
  output_dir = OUTPUT_DIR + mda + '/'
  if not os.path.exists( output_dir ) :
    os.makedirs( output_dir )

  output_file = output_dir + FILE_NAME 
  # run program cpu time
  cmd = 'ulimit -St ' + CPU_TIME 
  # run program memory size
  cmd += ' && ulimit -Sv ' + MEMORY_SIZE
  cmd += ' && ulimit -Sm ' + MEMORY_SIZE
  cmd += ' && ulimit -Sd ' + MEMORY_SIZE + ' ;'
  from calbox.cal_x.question.models import Question_IO
  question_io_list = Question_IO.objects.get_question_io( m_question )
  try :
    # get question I/O
    for list in question_io_list :
      mess = run_question( mda, cmd, output_file,  list.input_text.encode('utf-8'), list.output_text.encode('utf-8'), list.occult )
      # run error
      if mess :
        del_TEMP_OUTPUT_dir( mda )
        return mess

    del_TEMP_OUTPUT_dir( mda )
    return json_message( RUN_AND_CHECK_SUCCESS, RUN_OK )
  except :
    del_TEMP_OUTPUT_dir( mda )
    return json_message( 'Question no get', UNKNOW_ERR )

def run_question( mda, cmd, output_file, question_input, question_output, occult ):
  p = subprocess.Popen( args= 'cd ' + BINARY_DIR + mda + ' ; ' + cmd +' java ' + FILE_NAME,
                        stdin = subprocess.PIPE,
                        stdout = open( output_file , 'w' ),
                        stderr = subprocess.PIPE,
                        shell = True)
  p.stdin.write( question_input )
  p.stdin.close()
  p.wait()
  errm = p.stderr.read()
  if errm == '' :
    #return json_message( open( output_file, 'r' ).read(), 'run_OK')
    code_output = open( output_file, 'r' ).read()
    #return type(question_output ) 
    #return 'code_output :' + code_output + 'input :' + question_input + 'output :' + question_output
    if question_output.replace('\r\n', '\n') == code_output :
      return False
    else :
      if occult :
        return json_message( OCCULT_IO, RUN_OK )
      else :
        return json_message( '數據輸入 :' + question_input + '<<\n正確輸出 :' + question_output + '<<\n你程式輸出 :' + code_output + '<<', 'check_error' )
  else :
    if errm == 'CPU time limit exceeded\n' :
      return json_message( '', INFINITE_LOOP )

    return json_message( errm, RUN_ERR )


def style_check( code ):
  return ""
