# -*- coding: utf-8 -*-
import os
import subprocess
from compiler import compiler

class compiler_java(compiler):
  _FN = "Main"
  _FE = ".java"
  _LANG = 10
  _COM_TOOL = "javac"
  _RUNCMD = "java "
  _CMD = ''

  def compiler_code( self, cmd = '' ):
    file_code = self.FILE_DIR + self._mda + '/' + self._FN + self._FE
    if not os.path.exists( file_code ) :
      return self.NO_INPUT_FILE

    binary_dir =  self.BINARY_DIR + self._mda + '/'
    if not os.path.exists( binary_dir ) :
      os.makedirs( binary_dir )

    binary_file = binary_dir + self._FN
    pingPopen = subprocess.Popen(args= self._COM_TOOL + ' ' + file_code + ' -d '+ binary_dir + ' ' + cmd, shell=True
                               , stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    pingPopen.wait()
    self._compiler_mes = pingPopen.stderr.read()
    self._compiler_state = os.path.exists( binary_file + ".class" )
    return self._compiler_state

