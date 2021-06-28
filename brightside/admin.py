from django.contrib import admin
from .models import Patient, Reseptionist, Service, Bill, Appointment, Physician
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient', 'p_first_name', 'p_last_name', ]

@admin.register(Physician)
class PhysicianAdmin(admin.ModelAdmin):
    list_display = ['ph_id', 'ph_first_name', 'ph_last_name', 'ph_speciality',]

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [ 'appointment_date', 'appointment_time']



@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['bill_id', 'bill_date', 'bill_status','payment_method','total_pay']

@admin.register(Reseptionist)
class ReseptionistAdmin(admin.ModelAdmin):
    list_display = ['r_username', 'r_password',]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_price', 'physician']