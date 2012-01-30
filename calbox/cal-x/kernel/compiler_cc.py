# -*- coding: utf-8 -*-
import os
import subprocess
from conf import *
from re_message import json_message
def core( mda, user, code, question):
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
  
  code_file = open(  code_dir + FILE_NAME  + FE_CC , 'w' )
  code_file.write( code.encode('utf8') )
  code_file.close()

def complit( mda ):
  file_code = FILE_DIR + mda + '/' +FILE_NAME + FE_CC 
  if not os.path.exists( file_code ) :
    return 'Code NO EXISTS'

  binary_dir =  BINARY_DIR + mda + '/'
  if not os.path.exists( binary_dir ) :
    os.makedirs( binary_dir )
    
  pingPopen = subprocess.Popen(args='g++ '+ file_code + ' -o '+ binary_dir + FILE_NAME , shell=True, stderr=subprocess.PIPE)
  pingPopen.wait()
  return pingPopen.stderr.read()

def run( mda, question ):
  cmd = 'ulimit -St ' + CPU_TIME
  #cmd += ' && ulimit -Su ' + SOKET_NUM 
  cmd += ' && ulimit -Sv ' + MEMORY_SIZE
  cmd += ' && ulimit -Sm ' + MEMORY_SIZE
  cmd += ' && ulimit -Sd ' + MEMORY_SIZE + ' ;'

  output_dir = OUTPUT_DIR + mda + '/'
  if not os.path.exists( output_dir ) :
    os.makedirs( output_dir )

  output_file = output_dir + FILE_NAME
  p = subprocess.Popen( args= cmd + ' ' + BINARY_DIR + mda + '/' + FILE_NAME  ,
                        stdin = subprocess.PIPE,
                        stdout = open( output_file , 'w' ),
                        stderr = subprocess.PIPE,
                        shell = True)
  p.stdin.write('3\n')
  p.stdin.write('4\n')
  p.wait()
  try :
    errm = p.stderr.read()
    if errm == '' :
      return json_message( open( output_file, 'r' ).read(), 'run_OK')
    else :
      return json_message( errm, 'run_error' )
  except  :
    return json_message( 'except ?', '??' )

def style_check(  code ):
  return ""
