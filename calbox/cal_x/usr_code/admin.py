from django.contrib import admin
from calbox.cal_x.usr_code.models import Code, Code_Done

class Usr_Code_Admin( admin.ModelAdmin ):
  question = ( 'question', 'usr', 'code_text', 'lang', 'updatetime' )

class Usr_Code_Done_Admin( admin.ModelAdmin ):
  question = ( 'question', 'usr', 'code_text', 'lang', 'updatetime' )


admin.site.register(  Code, Usr_Code_Admin  )
admin.site.register(  Code_Done, Usr_Code_Done_Admin  )
