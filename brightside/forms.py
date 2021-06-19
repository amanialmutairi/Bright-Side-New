from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Appointment, Physician, Reseptionist, Service, Patient, Bill, Payment


class ReseptionistForm(ModelForm):
	class Meta:
		model = Reseptionist
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class PatientForm(ModelForm):
  class Meta:
    model = Patient
    fields = ['p_username', 'p_first_name', 'p_last_name', 'p_email', 'p_password']