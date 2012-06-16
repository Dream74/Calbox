from django.contrib import admin
from calbox.cal_x.usr_code.models import Code, Code_Done

class Usr_Code_Admin( admin.ModelAdmin ):
  list_display = ('question', 'usr', 'lang', 'updatetime')
  question = ( 'question', 'usr', 'code_text', 'lang', 'updatetime' )

class Usr_Code_Done_Admin( admin.ModelAdmin ):
  list_display = ('question', 'usr', 'lang', 'updatetime')
  list_filter = ('question', 'usr', 'lang')
  question = ( 'question', 'usr', 'code_text', 'lang', 'updatetime' )    
  actions = ['download_code']
  def download_code(self, request, queryset):
    from django.http import HttpResponse
    import zipfile, datetime, os
    from calbox.cal_x.kernel.conf import conf
    from calbox.cal_x.kernel.compiler import compiler as c_compiler
    from calbox.cal_x.kernel.compiler_cc import compiler_cc as cc_compiler
    from calbox.cal_x.kernel.compiler_java import compiler_java as java_compiler

    zippath = conf.BINARY_DIR + datetime.datetime.now().isoformat() +".zip"
    #zippath = "/dev/shm/ramdisk/temp/"+ datetime.datetime.now().isoformat() +".zip"
    file = zipfile.ZipFile(zippath, "w")
    for ques in queryset:
      s = ""
      if ques.lang == c_compiler().getLang() :
        s = c_compiler().getFE() 
      elif ques.lang == cc_compiler().getLang() :
        s = cc_compiler().getFE() 
      elif ques.lang == java_compiler().getLang() :
        s = java_compiler().getFE() 
      file.writestr(ques.usr.username + s , ques.code_text.encode('utf8') )

    file.close()
    
    response = HttpResponse(open(zippath, "rb").read(), mimetype="test/txt")
    response['Content-Disposition'] = 'attachment; filename=code.zip'
    os.remove(zippath)
    return response
    
  download_code.short_description = 'Download select Code'



admin.site.register(  Code, Usr_Code_Admin  )
admin.site.register(  Code_Done, Usr_Code_Done_Admin  )
