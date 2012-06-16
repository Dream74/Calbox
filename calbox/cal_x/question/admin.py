from django.contrib import admin
from calbox.cal_x.question.models import Question_Code, Question_IO, Question_Time

class Question_IO_Admin( admin.ModelAdmin ):
	#question_io = ( 'input_text', 'output_text', 'question' , 'usr', 'occult' )
  list_display = ('question', 'input_text', 'output_text', 'occult', 'usr')
  fieldsets = [ 
        ('input_text', {'fields':['input_text']}),
        ('output_text', {'fields':['output_text']}),
        ('question', {'fields':['question']}),
        ('Occult', {'fields':['occult']}),
        ('User', {'fields':['usr']}),
  ]  

  def save_model(self, request, obj, form, change):
    if change :
      obj.usr = request.user
      #obj.occult = False
      obj.save() 

class Question_IO_inline(admin.TabularInline):
  model = Question_IO
  extra = 1
  fieldsets = [ 
        ('input_text', {'fields':['input_text']}),
        ('output_text', {'fields':['output_text']}),
        ('question', {'fields':['question']}),
        ('Occult', {'fields':['occult']}),
  ]  
from django.contrib.auth.models import User
class Question_Code_Admin( admin.ModelAdmin ):
  list_display = ('title', 'occult', 'usr')
  fieldsets = [ 
        ('title', {'fields':['title']}),
        ('DOC', {'fields':['doc']}),
        ('Occult', {'fields':['occult']}),
  ] 
  def get_actions(self, request):
    actions = super(Question_Code_Admin, self).get_actions(request)
    if 'delete_selected' in actions:
      del actions['delete_selected']
    return actions

  actions = ['my_delete_selected']
  inlines = [Question_IO_inline]
  def save_model(self, request, obj, form, change):
    obj.usr = request.user
    return super(Question_Code_Admin, self).save_model(request, obj, form, change)

  def save_formset(self, request, form, formset, change):
    for form1 in formset.forms:
      form1.instance.usr = request.user
    return super(Question_Code_Admin, self).save_formset(request, form, formset, change)

  def my_delete_selected(self, request, queryset):
    for ques in queryset:
      ques.delete() 
  my_delete_selected.short_description = 'delete selected Question_Code test'

class Question_Time_Admin( admin.ModelAdmin ):
	question_time = ( 'start', 'end', 'perm'  )

admin.site.register( Question_Code, Question_Code_Admin )
admin.site.register( Question_Time, Question_Time_Admin )
