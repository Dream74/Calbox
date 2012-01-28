from django import forms

class UserForm(forms.Form):
	name = forms.CharField(max_length=32)
	password =  forms.CharField(max_length=32)
	email = forms.EmailField()
	build_date = forms.DateTimeField()

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()
