from django.contrib import admin
from .models import patient, reseptionist, service
# Register your models here.


#@admin.register(patient)
@admin.register(patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['p_username', 'p_fname', 'p_lname', 'p_email', 'p_password']


@admin.register(reseptionist)
class ReseptionistAdmin(admin.ModelAdmin):
    list_display = ['r_username', 'r_password']


@admin.register(service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_price']