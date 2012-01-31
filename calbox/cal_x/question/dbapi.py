from calbox.cal_x.question.models import Question_IO, Question_Code
from django.core import serializers
def get_all_question( ) :
  return Question_Code.objects.all().order_by('id')

def get_all_qeustion_json( id ):
	return serializers.serialize('json', Question_Code.objects.all(), fields=('title'), sort_keys = True, indent = 0, ensure_ascii = False )

def get_question_io( question_id ):
	return Question_IO.objects.filter(question = Question_Code.objects.get( id = question_id )  ).order_by( 'occult', 'id')	

