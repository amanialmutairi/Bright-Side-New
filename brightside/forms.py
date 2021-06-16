from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Appointment, Physician, Reseptionist, Service, Patient, Bill, Payment

class ReseptionistForm(ModelForm):
	class Meta:
		model = Reseptionist
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = Patient
		fields = '__all__'