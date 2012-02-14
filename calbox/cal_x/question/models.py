from django.db import models
from django.contrib.auth.models import User
class Question_Code( models.Model ) :
	title = models.CharField(max_length=100)
	doc = models.TextField()
	usr = models.ForeignKey( User )
	def __unicode__(self):
		return unicode(self.title)
	class Meta:
		permissions = (
			('R_question', 'can read question'),
		)

class Question_IO( models.Model ) :
	input_text = models.TextField( null = True, blank = True )
	output_text = models.TextField()
	question = models.ForeignKey( Question_Code ) 
	usr = models.ForeignKey( User )
	occult = models.BooleanField()
	def __unicode__(self):
		return unicode(self.question)
