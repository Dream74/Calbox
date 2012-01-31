from django.db import models
from django.contrib.auth.models import User
from calbox.cal_x.question.models import Question_Code

class Code( models.Model ) : 
  question = models.ForeignKey( Question_Code )
  usr = models.ForeignKey( User )
  code_text = models.TextField()
  lang = models.IntegerField( ) 
  updatetime = models.DateTimeField() 
  def __unicode__(self):
    return unicode(self.usr)
