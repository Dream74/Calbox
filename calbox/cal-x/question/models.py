from django.db import models
from django.contrib.auth.models import User
class Question_Code( models.Model ) :
	title = models.CharField(max_length=100)
	doc = models.TextField()
	usr = models.ForeignKey( User )
	def __unicode__(self):
		return self.title

class Question_IO( models.Model ) :
	input_text = models.TextField()
	output_text = models.TextField()
	question = models.ForeignKey( Question_Code ) 
	usr = models.ForeignKey( User )
	occult = models.BooleanField()
	def __unicode__(self):
		return self.usr
