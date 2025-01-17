
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Appointment, Physician, Reseptionist, Service, Patient, Bill

class CreateAppointmentAdmin(ModelForm):
  class Meta:
     model = Appointment
     fields = '__all__'
     widgets = {
      'appointment_date': DatePickerInput(),
      'appointment_time': TimePickerInput(),

    }

class CreateAppointmentUser(ModelForm):
  class Meta:
     model = Appointment
     fields = '__all__'
     widgets = {
      'reseptionist' : forms.HiddenInput(), 
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
		fields = ['username', 'email', 'password1']

class PatientForm(ModelForm):
  class Meta:
    model = Patient
    fields = '__all__'
    widgets = {
      'profile' : forms.HiddenInput(), }

#class BillForm(ModelForm):
 # class Meta:
  #  model = Bill
   # fields = ['bill_id','bill_date', 'bill_status' ,'total_pay', 'payment_method']

