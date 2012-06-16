# -*- coding: utf-8 -*-

#import os
#import subprocess
from compiler import compiler

class compiler_cc(compiler):
  _FE = ".cc"
  _LANG = 1
  _COM_TOOL = "g++"
  _RUNCMD = "./"
  _CMD = '-std=c++0x'
