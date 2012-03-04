from django.contrib import admin
from calbox.cal_x.question.models import Question_Code, Question_IO, Question_Time

class Question_Code_Admin( admin.ModelAdmin ):
    fieldsets = [ 
          ('title', {'fields':['title']}),
          ('DOC', {'fields':['doc']}),
          ('User', {'fields':['usr']}),
          ('Occult', {'fields':['occult']}),
    ]   
    actions = ['delete_seleted_Question_Code']

    def delete_seleted_Question_Code(self, request, queryset):
      for ques in queryset:
        ques.delete() 

class Question_IO_Admin( admin.ModelAdmin ):
	question_io = ( 'input_text', 'output_text', 'question' , 'usr', 'occult' )

class Question_Time_Admin( admin.ModelAdmin ):
	question_time = ( 'start', 'end', 'perm'  )

admin.site.register( Question_Code, Question_Code_Admin )
admin.site.register( Question_IO, Question_IO_Admin  )
admin.site.register( Question_Time, Question_Time_Admin )
admin.site.disable_action('delete_selected')
