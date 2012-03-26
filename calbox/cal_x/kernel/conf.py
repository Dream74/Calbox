#compliter conf
# -*- coding: utf-8 -*-
CAL_X_HOME = '/dev/shm/ramdisk/'
FILE_DIR = CAL_X_HOME + 'code/'
BINARY_DIR = CAL_X_HOME + 'TEMP/'
OUTPUT_DIR = CAL_X_HOME + 'output/'
FILE_NAME = 'Main'
FE_CC = '.cc'
FE_C = '.c'
FE_JAVA = '.java'
COM_C = 'gcc'
COM_CC = 'g++'
COM_JAVA = 'javac'

#run limit
CPU_TIME = '3' # 5 sec
CODE_FILE =  str( 64 * 1024 / 2 )  # 64 KB
MEMORY_SIZE = str( 500 * 1024 ) # 500MB
#SOKET_NUM = '10'

# json message type
OCCULT_IO = '你無法通過被隱藏的數據'
#run expect shell 
RUNCALSHELL = '/Users/DREAM/Desktop/CAL-X/cal_python_test/demo.sh'

LANG_C = 11
LANG_CC = 1
LANG_JAVA = 10

from shutil import rmtree
from os.path import exists
def del_TEMP_OUTPUT_dir( mda ):
  _dir = BINARY_DIR + mda + '/'
  if exists( _dir ) :
    rmtree( _dir )

  _dir = OUTPUT_DIR + mda + '/'
  if exists( _dir ) :
    rmtree( _dir )

