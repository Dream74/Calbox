# cal-x core conf
# -*- coding: utf-8 -*-

# cal-x temp dir
CAL_X_HOME = '/dev/shm/ramdisk/'
FILE_DIR = CAL_X_HOME + 'code/'
BINARY_DIR = CAL_X_HOME + 'TEMP/'
OUTPUT_DIR = CAL_X_HOME + 'output/'

# temp file name, subname
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

# error message
COM_ERR = 'Complit error'
STYPLE_ERR = 'Styple error'
RUN_ERR = 'Run time error'
UNKNOW_ERR = 'Unknow error'
INFINITE_LOOP = 'Infinite loop'
CHECK_ERR = 'Check error'
RUN_OK = 'Run OK'
# json message type
CODE_SIZE_LIMIT = '你的程式碼內容過長'
OCCULT_IO = '你無法通過被隱藏的數據'
RUN_AND_CHECK_SUCCESS = '你程式通過所有測試數據'
# code lang index
LANG_C = 11
LANG_CC = 1
LANG_JAVA = 10

def del_TEMP_OUTPUT_dir( mda ):
  from shutil import rmtree
  from os.path import exists
  _dir = BINARY_DIR + mda + '/'
  if exists( _dir ) :
    rmtree( _dir )

  _dir = OUTPUT_DIR + mda + '/'
  if exists( _dir ) :
    rmtree( _dir )

