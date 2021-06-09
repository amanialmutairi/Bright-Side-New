from django.db import models

# Create your models here.

#class reseptionist(models.Model):
class reseptionist(models.Model):
  r_username = models.CharField(max_length=50, unique=True, primary_key=True)
  r_password = models.CharField(max_length=100)

  def __str__(self):
        return self.r_username
#class appointment(models.Model):

#class service(models.Model):
class service(models.Model):
  service_name = models.CharField(max_length=50)
  service_price = models.DecimalField(max_digits=8, decimal_places=2)
  
  def __str__(self):
        return self.service_name

#class patient(models.Model):
class patient(models.Model):
    p_username = models.CharField(max_length=50, unique=True, primary_key=True)
    p_fname = models.CharField(max_length=50)
    p_lname =  models.CharField(max_length=50)
    p_email = models.EmailField(max_length= 100, unique=True)
    p_password = models.CharField(max_length=100)

    def __str__(self):
        return self.p_fname

#class physician(models.Model):

#class bill(models.Model):

#class payment(models.Model):