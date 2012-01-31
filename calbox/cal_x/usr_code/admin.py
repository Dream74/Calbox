from django.contrib import admin
from calbox.cal_x.usr_code.models import Code

class Usr_Code_Admin( admin.ModelAdmin ):
  question = ( 'question', 'usr', 'code_text', 'lang', 'updatetime' )


admin.site.register(  Code, Usr_Code_Admin  )
