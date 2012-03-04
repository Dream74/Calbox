from django.db import models
from django.contrib.auth.models import User
from calbox.cal_x.question.models import Question_Code
class CodeManager(models.Manager):
  def get_my_question_code(self, m_usr, m_lang, question_id ):
    return Code.objects.filter( usr = m_usr, lang = m_lang, question = Question_Code.objects.get( id = question_id )).order_by('-updatetime')[0]

  def insert_code( self, m_usr, m_lang, m_code, question_id ):
    import datetime
    Code( usr = m_usr, lang = m_lang, question = Question_Code.objects.get( id = question_id ), code_text = m_code, updatetime = datetime.datetime.now()  ).save()

class Code( models.Model ) : 
  question = models.ForeignKey( Question_Code )
  usr = models.ForeignKey( User )
  code_text = models.TextField()
  lang = models.IntegerField( ) 
  updatetime = models.DateTimeField() 
  objects = CodeManager()
  def __unicode__(self):
    return unicode(self.usr)
