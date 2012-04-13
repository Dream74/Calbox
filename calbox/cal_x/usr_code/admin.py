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
    pass
    #for ques in queryset:
    #  ques.delete()
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
