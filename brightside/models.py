from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class reseptionist(models.Model):
class Reseptionist(models.Model):
  r_username = models.CharField(max_length=50, unique=True, primary_key=True)
  r_password = models.CharField(max_length=100)

  def __str__(self):
        return self.r_username

#class physician(models.Model):
class Physician(models.Model):
  Speciality = (
        (0, 'General Dentist'),
        (1, 'Periodontist'),
        (2, 'Oral and Maxillofacial Surgeon'),
        (3, 'Nurse'),

    )
  ph_id = models.CharField(max_length=15, unique=True, verbose_name='ID')
  ph_first_name = models.CharField(max_length=50, verbose_name='First name')
  ph_last_name =  models.CharField(max_length=50, verbose_name='Last name')
  ph_speciality =  models.IntegerField(choices=Speciality, default=0, verbose_name='Speciality')

  def __str__(self):
    return f'{self.ph_first_name}  {self.ph_last_name} '

class Ph_service(models.Model):
  physician = models.ForeignKey('Physician', on_delete=models.CASCADE)
  service = models.ForeignKey('Service', on_delete=models.CASCADE)

#class service(models.Model):
class Service(models.Model):
  service_name = models.CharField(max_length=50)
  service_price = models.DecimalField(max_digits=8, decimal_places=2)
  physician = models.ForeignKey('Physician', on_delete=models.CASCADE)

  def __str__(self):
        return self.service_name

#class patient(models.Model):
class Patient(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    p_first_name = models.CharField(max_length=50, verbose_name='First name')
    p_last_name =  models.CharField(max_length=50, verbose_name='Last name')


    def __str__(self):
        return self.p_first_name


#class appointment(models.Model):
class Appointment(models.Model):
  appointment_date = models.DateField(null=True)
  appointment_time = models.TimeField(null=True)
  patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
  reseptionist = models.ForeignKey('Reseptionist', on_delete=models.SET_NULL, blank=True, null=True)
  service = models.ForeignKey('Service', on_delete=models.CASCADE)
  physician = models.ForeignKey('Physician', on_delete=models.CASCADE)

  #class bill(models.Model):
class Bill(models.Model):
  payment_method = (
        (0, 'VISA'),
        (1, 'Master Card'),
        (2, 'Cash'),
        (3, 'Knet')
    )
  STATUS = (
        (0, 'Paid'),
        (1, 'Unpaid'),
    )
  bill_id = models.CharField(max_length=15, unique=True)
  bill_date = models.DateTimeField(null=True)
  bill_status = models.IntegerField(choices=STATUS, default=1)
  total_pay = models.DecimalField(max_digits=8, decimal_places=2)
  payment_method = models.IntegerField(choices=payment_method, default=0)

  appointment = models.OneToOneField(Appointment, 
          on_delete = models.CASCADE)
  patient = models.ForeignKey('Patient', on_delete=models.CASCADE)

