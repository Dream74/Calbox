from django import forms

class Question_Code( forms.Form ) : 
  title = forms.CharField(max_length=100)
  doc = froms.TextField()
  usr = froms.ForeignKey( User )
  def __unicode__(self):
    return unicode(self.title)

class Question_IO( forms.Form ) : 
  input_text = froms.TextField( null = True)
  output_text = froms.TextField()
  question = froms.ForeignKey( Question_Code ) 
  usr = froms.ForeignKey( User )
  occult = froms.BooleanField()
  def __unicode__(self):
    return unicode(self.question)
