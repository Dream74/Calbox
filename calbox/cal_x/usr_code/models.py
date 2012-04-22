from django.db import models
from django.contrib.auth.models import User
from calbox.cal_x.question.models import Question_Code
import datetime
class CodeManager(models.Manager):
  def insert_code( self, m_usr, m_lang, m_code, question_id ):
    try :
      code = Code.objects.get( usr = User.objects.get( username = m_usr ), lang = m_lang, question = Question_Code.objects.get( id = question_id ) )
      code.code_text = m_code
      code.updatetime = datetime.datetime.now()
      code.save()
    except Code.DoesNotExist:
      Code( usr = m_usr, lang = m_lang, question = Question_Code.objects.get( id = question_id ), code_text = m_code, updatetime = datetime.datetime.now()  ).save()

  def getcode_text( self, usr, lang, question ):
    try :
      return Code.objects.get( usr = User.objects.get( username = usr ), lang = lang, question = Question_Code.objects.get( id = question )  ).code_text
    except Code.DoesNotExist:
      return ""

class Code( models.Model ) : 
  question = models.ForeignKey( Question_Code )
  usr = models.ForeignKey( User)
  code_text = models.TextField()
  lang = models.IntegerField() 
  updatetime = models.DateTimeField() 
  objects = CodeManager()
  def __unicode__(self):
    return unicode(self.usr)

  def __str__(self):
    return str(self.usr)

class Code_DoneManager(models.Manager):
  def get_my_question_code(self, m_usr, m_lang, question_id ):
    return Code.objects.filter( usr = m_usr, lang = m_lang, question = Question_Code.objects.get( id = question_id )).order_by('-updatetime')[0]

  def insert_code( self, m_usr, m_lang, m_code, question_id ):
    Code_Done( usr = m_usr, lang = m_lang, question = Question_Code.objects.get( id = question_id ), code_text = m_code, updatetime = datetime.datetime.now()  ).save()

class Code_Done( models.Model ) : 
  question = models.ForeignKey( Question_Code )
  usr = models.ForeignKey( User )
  code_text = models.TextField()
  lang = models.IntegerField() 
  updatetime = models.DateTimeField() 
  objects = Code_DoneManager()
  def __unicode__(self):
    return unicode(self.usr)

  def __str__(self):
    return str(self.usr)

