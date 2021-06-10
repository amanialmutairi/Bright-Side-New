from django.db import models

# Create your models here.

#class reseptionist(models.Model):
class reseptionist(models.Model):
  r_username = models.CharField(max_length=50, unique=True, primary_key=True)
  r_password = models.CharField(max_length=100)

  def __str__(self):
        return self.r_username

#class physician(models.Model):


#class service(models.Model):
class service(models.Model):
  service_name = models.CharField(max_length=50)
  service_price = models.DecimalField(max_digits=8, decimal_places=2)
  #physician = models.ForeignKey('physician', on_delete=models.CASCADE)

  def __str__(self):
        return self.service_name

#class patient(models.Model):
class patient(models.Model):
    p_username = models.CharField(max_length=50, unique=True, primary_key=True)
    p_first_name = models.CharField(max_length=50)
    p_last_name =  models.CharField(max_length=50)
    p_email = models.EmailField(max_length= 100, unique=True)
    p_password = models.CharField(max_length=100)

    def __str__(self):
        return self.p_first_name



#class bill(models.Model):
class Bill(models.Model):
  bill_id = models.CharField(max_length=15, unique=True)
  bill_date = models.DateTimeField(null=True)
#class payment(models.Model):
class Payment(models.Model):
  receipt_id = models.CharField(max_length=15, unique=True)
  payment_method = (
        (0, "VISA"),
        (1, "Master Card"),
        (2, "Cash"),
        (3, "Knet")
    )
  total_pay = models.CharField(max_length=15)
  payment_date = models.DateTimeField(null=True)
#class appointment(models.Model):
class Appointment(models.Model):
  appointment_id = models.CharField(max_length=15, unique=True)
  appointment_date = models.DateField(null=True)
  appointment_time = models.TimeField(null=True)
  