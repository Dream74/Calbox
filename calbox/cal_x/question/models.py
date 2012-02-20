from django.db import models
from django.contrib.auth.models import User, Permission
class Question_Code( models.Model ) :
	title = models.CharField(max_length=100)
	doc = models.TextField()
	usr = models.ForeignKey( User )
	perm = models.OneToOneField( Permission )
	def __unicode__(self):
		return unicode(self.title)
	
	def __str__(self):
		return self.title 

	def save(self, *args, **kwargs):
		#try :
		#	Permission.objects.get( name=self.title )
		#except Permission.DoesNotExist:
		if not Permission.objects.filter( name=self.title ):
			from django.contrib.contenttypes.models import ContentType
			p = Permission( name=self.title, content_type=ContentType.objects.get( name='question_ code'), codename=self.title+'_'+ self.usr.username)
			p.save()
			self.perm = p 
		super(Question_Code, self).save()

	def delete(self, *args, **kwargs):
		Permission.objects.get(name=self.title).delete()
		Question_IO.objects.filter( question=self ).delete()
		super(Question_Code, self).delete()

class Question_IO( models.Model ) :
	input_text = models.TextField( null = True, blank = True )
	output_text = models.TextField()
	question = models.ForeignKey( Question_Code ) 
	usr = models.ForeignKey( User )
	occult = models.BooleanField()
	def __unicode__(self):
		return unicode(self.question)
	def __str__(self):
		return self.question
