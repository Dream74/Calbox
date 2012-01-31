from calbox.cal_x.usr_code.models import Code
from calbox.cal_x.question.models import Question_Code
from django.contrib.auth.models import User
import datetime
def get_my_question_code( m_usr, m_lang, question_id ):
  return Code.objects.filter( usr = m_usr, lang = m_lang, question = Question_Code.objects.get( id = question_id )).order_by('-updatetime')[0]

def insert_code( m_usr, m_lang, m_code, question_id ):
  Code( usr = m_usr, lang = m_lang, question = Question_Code.objects.get( id = question_id ), code_text = m_code, updatetime = datetime.datetime.now()  ).save()
