from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import time
from django.utils import timezone

class contact_form(models.Model):
	Mr = 'Mr'
	Mrs = 'Mrs'
	Ms = 'Ms'
	selected_title = (
		(Mr,'Mr'),
		(Mrs,'Mrs'),
		(Ms,'Ms')

	)
	title = models.CharField(max_length = 3,choices = selected_title,default = Ms)
	name = models.CharField(max_length = 100)
	email = models.EmailField(max_length=254)
	password = models.CharField(max_length = 255)
	phone_num = PhoneNumberField(null=False, blank=False, unique=True)
	add = models.CharField(max_length = 255)
	creation_date = models.DateTimeField(auto_now = True)