from django.db import models

# Create your models here.

#class reseptionist(models.Model):
class Reseptionist(models.Model):
  r_username = models.CharField(max_length=50, unique=True, primary_key=True)
  r_password = models.CharField(max_length=100)

  def __str__(self):
        return self.r_username

#class physician(models.Model):
class Physician(models.Model):
  ph_id = models.CharField(max_length=15, unique=True)
  ph_first_name = models.CharField(max_length=50)
  ph_last_name =  models.CharField(max_length=50)
  ph_speciality =  models.CharField(max_length=30)

  def __str__(self):
    return f" First Name: {self.ph_first_name} - Last Name: {self.ph_last_name} - Speciality: {self.ph_speciality}"

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
    p_username = models.CharField(max_length=50, unique=True, primary_key=True)
    p_first_name = models.CharField(max_length=50)
    p_last_name =  models.CharField(max_length=50)
    p_email = models.EmailField(max_length= 100, unique=True)
    p_password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.p_first_name



#class bill(models.Model):
class Bill(models.Model):
  STATUS = (
        (0, "Paid"),
        (1, "Unpaid"),
    )
  bill_id = models.CharField(max_length=15, unique=True)
  bill_date = models.DateTimeField(null=True)
  bill_status = models.IntegerField(choices=STATUS, default=1)

#class payment(models.Model):
class Payment(models.Model):
  payment_method = (
        (0, "VISA"),
        (1, "Master Card"),
        (2, "Cash"),
        (3, "Knet")
    )
  STATUS = (
        (0, "Paid"),
        (1, "Unpaid"),
    )
  receipt_id = models.CharField(max_length=15, unique=True)
  total_pay = models.CharField(max_length=15)
  payment_date = models.DateTimeField(null=True)
  status = models.IntegerField(choices=STATUS, default=1)
  payment_method = models.IntegerField(choices=STATUS, default=0)
  patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
  

#class appointment(models.Model):
class Appointment(models.Model):
  appointment_id = models.CharField(max_length=15, unique=True)
  appointment_date = models.DateField(null=True)
  appointment_time = models.TimeField(null=True)
  patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
  reseptionist = models.ForeignKey('Reseptionist', on_delete=models.CASCADE)
  service = models.ForeignKey('Service', on_delete=models.CASCADE)
  physician = models.ForeignKey('Physician', on_delete=models.CASCADE)