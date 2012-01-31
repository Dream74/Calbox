# -*- coding: utf-8 -*-
import os
import subprocess
from conf import *
from re_message import json_message
from calbox.cal_x.question.dbapi import get_all_question, get_question_io
def core( mda, user, code, question):
  #return get_all_question( 1 )[0].id
  if len( code ) > CODE_FILE :
    return json_message( 'Code size limit exceeded', 'Code size limit')
  update_code( mda, code )
  com_msn = complit( mda )
  if com_msn == "" :
    style_msn = style_check( code )
    if style_msn == "" :
      return run( mda, question )
    else :
     return json_message( style_msn, 'Styple error')
  else :
   return json_message( com_msn, 'Complit error')

def update_code( mda, code ):  
  code_dir = FILE_DIR + mda + '/' 
  if not os.path.exists( code_dir ):
    os.makedirs( code_dir )
  
  code_file = open(  code_dir + FILE_NAME  + FE_C , 'w' )
  code_file.write( code.encode('utf8') )
  code_file.close()

def complit( mda ):
  file_code = FILE_DIR + mda + '/' +FILE_NAME + FE_C 
  if not os.path.exists( file_code ) :
    return 'Code NO EXISTS'

  binary_dir =  BINARY_DIR + mda + '/'
  if not os.path.exists( binary_dir ) :
    os.makedirs( binary_dir )
    
  pingPopen = subprocess.Popen(args='gcc '+ file_code + ' -o '+ binary_dir + FILE_NAME , shell=True, stderr=subprocess.PIPE)
  pingPopen.wait()
  return pingPopen.stderr.read()

def run( mda, m_question ):
  output_dir = OUTPUT_DIR + mda + '/'
  if not os.path.exists( output_dir ) :
    os.makedirs( output_dir )

  output_file = output_dir + FILE_NAME 
  cmd = 'ulimit -St ' + CPU_TIME 
  #cmd += ' && ulimit -Su ' + SOKET_NUM 
  cmd += ' && ulimit -Sv ' + MEMORY_SIZE
  cmd += ' && ulimit -Sm ' + MEMORY_SIZE
  cmd += ' && ulimit -Sd ' + MEMORY_SIZE + ' ;'
  question_io_list = get_question_io( m_question ) 
  try :
    for list in question_io_list :
      mess = run_question( mda, cmd, output_file,  list.input_text.encode('utf-8'), list.output_text.encode('utf-8'), list.occult ) 
      if mess :
        return mess

    return json_message( 'Success', 'OK' )
  except :
    return json_message( 'Question no get', '??' )

def run_question( mda, cmd, output_file, question_input, question_output, occult ):
  #return 'mda :' + mda + 'cmd :' + cmd + 'input :' + question_input + 'output :' + question_output
  p = subprocess.Popen( args= cmd + ' ' + BINARY_DIR + mda + '/' + FILE_NAME  ,
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
    if question_output == code_output :
      return False
    else :
      if occult :
        return json_message( '隱藏數據不給看', 'Run_OK' )
      else :
        return json_message( '數據輸入 :' + question_input + '正確輸出 ：' + question_output + '你程式輸出 :' + code_output, 'check_error' ) 
  else :
    return json_message( errm, 'run_time_error' )

def style_check( code ):
  return ""
