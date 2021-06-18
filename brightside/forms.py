from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Appointment, Physician, Reseptionist, Service, Patient, Bill, Payment

class CreateAppointment(ModelForm):
  class Meta:
     model = Appointment
     fields = '__all__'
     widgets = {
      'appointment_date': DatePickerInput(),
      'appointment_time': TimePickerInput(),

    }

class ReseptionistForm(ModelForm):
	class Meta:
		model = Reseptionist
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']