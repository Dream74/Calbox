# -*- coding: utf-8 -*-
import os
import subprocess
from conf import conf
class compiler(conf):
  _FN = "main"
  _FE = ".c"
  _LANG = 11
  _CMD = '-std=c99'
  _COM_TOOL = "gcc"
  _RUNCMD = "./"

  _question = None
  _style_msn = None
  _compiler_state = None
  _compiler_mes = None 
  _run_state = None
  _run_mes = None 
  _Rout = None 
  _Qout = None 
  _rate_mes = None
  _mda = None
  _usr = None
  _ulimit = None  

  def getQout(self):
    return self._Qout

  def getRout(self):
    return self._Rout

  def getLang(self):
    return self._LANG

  def getFN(self):
    return self._FN

  def getFE(self):
    return self._FE

  def __init__(self, usr = None, code = None, question = None):
    if usr is None :	  
      import datetime
      usr = datetime.datetime.now().isoformat()
    self._usr = usr 
    self._question = question
    self.mda( usr, question )
    if not code is None:
      self.code( code ) 

    # run program cpu time
    self._ulimit = 'ulimit -St ' + self.CPU_TIME 
    # run program memory size
    self._ulimit += ' && ulimit -Sv ' + self.MEMORY_SIZE
    self._ulimit += ' && ulimit -Sm ' + self.MEMORY_SIZE
    self._ulimit += ' && ulimit -Sd ' + self.MEMORY_SIZE + ' ;'
	
  def getRunMes(self):
    return self._run_mes 

  def getRunState(self):
    return self._run_state

  def getComMes(self):
    return self._compiler_mes

  def getComState(self):
    return self._compiler_state

  # cal-x core update-> complite-> style-> run (check I/O)
  # input : mda: temp path, user : user name, code : user code, question :user select question
  def kernel( self, question = None, IOlist = None, IO_rate = False, mcode = None ):
    if not mcode is None and not self.code( mcode ) :
	    return self.message( self.CODE_SIZE_LIMIT )
  
    self.question( question )

    # complite code from temp
    if self.compiler_code( self._CMD ) :
      # styple code 
      if self.style_check( self.code() ) :
        if not IOlist is None:
          return self.run_list( IOlist = IOlist, IO_rate = IO_rate )
        elif not self._question is None:
          return self.run_list( question, IO_rate = IO_rate )
        return self.message( self.UNKNOW_ERR, "no get question and IOlist" )
      else :
        return self.message( self.STYPLE_ERR, style_msn)
    else :
      return self.message( self.COM_ERR, self._compiler_mes )
	  
  # return user code from temp
  def code( self, code = None):
 	  # get code
    if code is None :
      file_path = self.FILE_DIR + self._mda + "/" + self._FN  + self._FE
      if not os.path.exists( self.FILE_DIR ) or not os.path.exists( file_path ):
        return ""
  
      code_file = open(  file_path , 'r' )
      return code_file.read()
    # set code
    else :
      if len( code ) > self.CODE_FILE :
        self._compiler_mes = self.CODE_SIZE_LIMIT
        return False

      code_dir = self.FILE_DIR + self._mda + '/' 
      if not os.path.exists( code_dir ):
        os.makedirs( code_dir )
  
      code_file = open(  code_dir + self._FN  + self._FE , 'w' )
      code_file.write( code.encode('utf8') )
      code_file.close()
      return True
	
  def question( self, question = None ):
    if question is None:
      return self._question   
    else :
      self._question = question 

  def __clear( self ) :
    from shutil import rmtree
    from os.path import exists
    self._dir = self.BINARY_DIR + self._mda + '/'
    if exists( self._dir ) :
      rmtree( self._dir )

    self._dir = self.OUTPUT_DIR + self._mda + '/'
    if exists( self._dir ) :
      rmtree( self._dir )
	  
    self._dir = self.FILE_DIR + self._mda + '/'
    if exists( self._dir ) :
      rmtree( self._dir )

  def __del__( self ) :
	  self.__clear() 

  def __str__( self ) :
    pass

  def __unicode__( self ) :
    pass

  # 我想用字典方式回傳error	
  def message( self, mess_type, message = "", IO_rate = False ) :
    import json
    #import re
    if IO_rate :
      return json.dumps( self._rate_mes , ensure_ascii = False)

    #return json.dumps({"message": re.compile( r'.+[\\\/]').sub( '', message ), "type": mess_type, "compiler_warn": re.compile( r'.+[\\\/]').sub( '', self._compiler_mes ) }, ensure_ascii = False)
    return json.dumps({"message": message , "type": mess_type, "compiler_warn": self._compiler_mes }, ensure_ascii = False)
	  # debug 排版用
    #return json.dumps({"message": re.compile( r'.+[\\\/]').sub( '', message ), "type": mess_type, "compiler_warn": re.compile( r'.+[\\\/]').sub( '', self.__compiler_mes ) }, sort_keys=True, indent=4)


  # cal-x ( lang, user, question) to dir path
  def mda( self, usr = None, question = None) :
    if usr is None and question is None :
	    return self._mda 
	
    import datetime
    from hashlib import md5
    self._mda = md5( datetime.datetime.now().isoformat().encode('utf-8') ).hexdigest()
  
  def compiler_code( self, cmd = '' ):
    file_code = self.FILE_DIR + self._mda + '/' + self._FN + self._FE 
    if not os.path.exists( file_code ) :
      return self.NO_INPUT_FILE

    binary_dir =  self.BINARY_DIR + self._mda + '/'
    if not os.path.exists( binary_dir ) :
      os.makedirs( binary_dir )
    
    binary_file = binary_dir + self._FN
    pingPopen = subprocess.Popen(args= self._COM_TOOL + ' ' + file_code + ' -o '+ binary_file + ' ' + cmd, shell=True
	                             , stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    pingPopen.wait()
    self._compiler_mes = pingPopen.stderr.read()
    self._compiler_state = os.path.exists( binary_file ) 
    return self._compiler_state

  # run all I/O, and check 
  def run_list( self, question = None, IOlist = None, IO_rate = False):
    self.question( question ) 
    if self._question is None and IOlist is None :
      return self.message( self.UNKNOW_ERR, 'Run No IO list')
    
    if IO_rate :
      self._rate_mes = []
    try :
      # check all question I/O
      if not IOlist is None:
        for list in IOlist :
          # run error
          IOinput = list["input"].encode('utf-8')
          IOoutput = list["output"].encode('utf-8')
          occult = False
          if not self.run( IOinput, IOoutput, occult ) and not IO_rate:
            return self.message( self.getRunState(), self.getRunMes() )
          if IO_rate:
            self._rate_mes += [ { "message" : self.getRunMes(), "type" : self.getRunState() } ]
      else :
        from calbox.cal_x.question.models import Question_IO
        question_io_list = None
        try :
          question_io_list = Question_IO.objects.get_question_io( self._question ) 
        except Question_IO.DoesNotExist :
          return self.message( self.UNKNOW_ERR, 'Question no get!!!')
        for list in question_io_list :
          IOinput = list.input_text.encode('utf-8')
          IOoutput = list.output_text.encode('utf-8')
          occult = list.occult
          if not occult or self.RUN_OCCULT_INPUT_LIST  :
            if not self.run( IOinput, IOoutput, occult ) and not IO_rate:
              return self.message( self.getRunState(), self.getRunMes() )
            if IO_rate:
              self._rate_mes += [ { "message" : self.getRunMes(), "type" : self.getRunState() } ]

      return self.message( self.RUN_OK, self.RUN_AND_CHECK_SUCCESS, IO_rate )
    except :
      return self.message( self.UNKNOW_ERR, 'UNKOW_ERR!!!')
	  
  def run( self, question_input = "", question_output = "",  occult = False ):
    output_dir = self.OUTPUT_DIR + self._mda + '/'
    if not os.path.exists( output_dir ) :
      os.makedirs( output_dir )

	
    output_file = output_dir + self._FN
    # ulimit -St CPU_TIME && -SV MEMORY_SIZE ... /XXX/code/mda/Main.c 
    p = subprocess.Popen( args= 'cd '+ self.BINARY_DIR + self._mda + ' ; '+ self._ulimit +  ' ' + self._RUNCMD + self._FN  ,
                        stdin = subprocess.PIPE,
                        stdout = open( output_file , 'w' ),
                        stderr = subprocess.PIPE,
                        shell = True)
    p.stdin.write( question_input )
    p.stdin.close()
    p.wait()
    errm = p.stderr.read()
    if errm == '' :
      code_output = open( output_file, 'r' ).read()
	    #window new line \r\n replace to linux \n
      if question_output.replace('\r\n', '\n') == code_output.replace('\r\n', '\n') :
        return self.run_state( self.RUN_OK, self.RUN_AND_CHECK_SUCCESS )
      else :
        if occult :
          self._Qout = self.OCCULT_IO
          self._Rout = code_output
          return self.run_state( self.COMPARE_ERR, self.OCCULT_IO )
        else :
          self._Qout = question_output
          self._Rout = code_output
          return self.run_state( self.COMPARE_ERR, '數據輸入 :' + question_input + '<<\n正確輸出 :' + question_output + '<<\n你程式輸出 :' + code_output + '<<' ) 
    else :
      if errm == 'CPU time limit exceeded\n' :
        return self.run_state( self.INFINITE_LOOP ) 

      return self.run_state( self.RUN_ERR, errm ) 

  def run_state( self, state , mes=""):
    self._run_state = state
    self._run_mes = mes
    return self._run_state == self.RUN_OK

  def style_check( self, code ) :
    return True
