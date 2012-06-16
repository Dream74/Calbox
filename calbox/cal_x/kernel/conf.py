# -*- coding: utf-8 -*-
class conf:
  # cal-x temp dir
  CAL_X_HOME = '/dev/shm/ramdisk/'
  FILE_DIR = CAL_X_HOME + 'code/'
  BINARY_DIR = CAL_X_HOME + 'temp/'
  OUTPUT_DIR = CAL_X_HOME + 'output/'

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
  COMPARE_ERR = 'Compare error'
  RUN_OK = 'Run OK'
  # json message type
  CODE_SIZE_LIMIT = '你的程式碼內容過長'
  OCCULT_IO = '你無法通過被隱藏的數據'
  RUN_AND_CHECK_SUCCESS = '你程式通過所有測試數據'
  
