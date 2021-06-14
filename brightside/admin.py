from django.contrib import admin
from .models import Patient, Reseptionist, Service, Bill
# Register your models here.


#@admin.register(patient)
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['p_username', 'p_first_name', 'p_last_name', 'p_email', 'p_password']

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['bill_id', 'bill_date', 'bill_status']

@admin.register(Reseptionist)
class ReseptionistAdmin(admin.ModelAdmin):
    list_display = ['r_username', 'r_password']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_price']