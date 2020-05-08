from django import forms 
from phonenumber_field.modelfields import PhoneNumberField
from .models import contact_form

class form_input(forms.ModelForm):
	phone = PhoneNumberField()
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = contact_form
		fields = [
			'title',
			'name',
			'email',
			'password',
			'phone_num',
			'add'
		]