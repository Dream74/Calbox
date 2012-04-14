from django.db import models
from django.contrib.auth.models import User, Permission

class CodeManager(models.Manager):
  def get_all_question(self):
    return Question_Code.objects.all().order_by('id')

  def get_all_qeustion_json( self, id ):
    from django.core import serializers
    return serializers.serialize('json', Question_Code.objects.all(), fields=('title'), sort_keys = True, indent = 0, ensure_ascii = False )

  def get_question_doc( self, q_id ):
    try :
      return Question_Code.objects.get( id = q_id ).doc
    except Question_Code.DoesNotExist:
      return "No Doc"

  def get_usr_question( self, usr ):
    q_list = []
    u = User.objects.get( username=usr)
    s_perm = u.user_permissions.all()
    for ques in Question_Code.objects.filter( occult=False):
      if ques.perm in s_perm:
        q_list.append(ques)
      else :
        for group in u.groups.all():
          if ques.perm in group.permissions.all() :
            q_list.append(ques)
    return q_list

class Question_Code( models.Model ) :
  title = models.CharField(max_length=100)
  doc = models.TextField()
  usr = models.ForeignKey( User )
  perm = models.OneToOneField( Permission )
  occult = models.BooleanField()
  objects = CodeManager()
  def __unicode__(self):
    return unicode(self.title)

  def __str__(self):
    return self.title 

  def save(self, *args, **kwargs):
    #try :
    #	Permission.objects.get( name=self.title )
    # except Permission.DoesNotExist:
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

class IOManager(models.Manager):
  def get_question_io( self, question_id ):
    return Question_IO.objects.filter(question = Question_Code.objects.get( id = question_id )  ).order_by( 'occult', 'id')

class Question_IO( models.Model ) :
  input_text = models.TextField( blank = True )
  output_text = models.TextField()
  question = models.ForeignKey( Question_Code ) 
  usr = models.ForeignKey( User )
  occult = models.BooleanField()
  objects = IOManager()
  def __unicode__(self):
    return unicode(self.question)
  def __str__(self):
    return self.question

class TimeManager(models.Manager):
  pass

class Question_Time( models.Model ):
  start = models.DateTimeField()
  end = models.DateTimeField()
  perm = models.OneToOneField( Permission )
  objects = TimeManager()
  def __unicode__(self):
    return unicode(self.perm)
  def __str__(self):
    return self.perm
