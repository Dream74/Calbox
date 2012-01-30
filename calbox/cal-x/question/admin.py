from django.contrib import admin
from question.models import Question_Code, Question_IO

class Question_Code_Admin( admin.ModelAdmin ):
	question = ('title', 'doc', 'usr' )

class Question_IO_Admin( admin.ModelAdmin ):
	question_io = ( 'input_text', 'output_text', 'question' , 'usr', 'occult' )

#admin.site.register( Question_Code, Question_Code_Admin )
#admin.site.register( Question_IO, Question_IO_Admin  )
