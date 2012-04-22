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
    from calbox.cal_x.kernel.conf import *
    zippath = "/dev/shm/ramdisk/TEMP/"+ datetime.datetime.now().isoformat() +".zip"
    file = zipfile.ZipFile(zippath, "w")
    for ques in queryset:
      if ques.lang == LANG_C :
        file.writestr(ques.usr.username+FE_C , ques.code_text.encode('utf8') )
      elif ques.lang == LANG_CC :
        file.writestr(ques.usr.username+FE_CC , ques.code_text.encode('utf8') )
      elif ques.lang == LANG_JAVA :
        file.writestr(ques.usr.username+FE_JAVA , ques.code_text.encode('utf8') )
      else :
        file.writestr(ques.usr.username , ques.code_text.encode('utf8') )

    file.close()
    
    response = HttpResponse(open(zippath, "rb").read(), mimetype="test/txt")
    response['Content-Disposition'] = 'attachment; filename=code.zip'
    os.remove(zippath)
    return response
    
    #html += str( ques.updatetime ) + "<br>"
    #return HttpResponse(html)
    """def test( request ):
    #image_data = open("/path/to/my/image.png", "rb").read()
    #return HttpResponse(image_data, mimetype="test/txt")
    if request.user.is_authenticated():
      m_user = request.user.username
  else :
    m_user = datetime.datetime.now().isoformat()
  m_lang = '11'
  m_question = '1'
  html = 'lang :%s<br>user :%s <br>qustion :%s' % ( m_lang, m_user, m_question )
  if m_user != '' and m_question != '' and m_lang != '' :
    return HttpResponse(Code.objects.filter()[0].code_text, mimetype="text/txt")
    #return HttpResponse('finally')
  else :
    html = 'have been space'
    return HttpResponse(html)
"""
  download_code.short_description = 'Download select Code'



admin.site.register(  Code, Usr_Code_Admin  )
admin.site.register(  Code_Done, Usr_Code_Done_Admin  )
