from django.urls import path
from . import views


urlpatterns = [
  
  path('home/profile/<int:profile_id>/', views.user_profile, name='profile'),
  path('home/profile/', views.profile_path, name='profile_path'),

  path('delete/appointment/', views.manage_view, name='manage'),
  path('booking/', views.booking_admin, name='admin-booking'),
  path('all_appointments/', views.view_all_apt, name='all_appointments'),
  path('home/', views.booking_user, name='home'),
  path('index/', views.index, name='index'),
  path('delete/appointment/<int:apt_id>/', views.delete_appointment),
  path('patient/detail', views.patient_list_view, name= 'patient-detail'),
  path('user/bill/<int:id>/' , views.bill_view, name='user-bill'),
  path('create/patient/' , views.create_patient_admin, name='create-patient'),
  path('create/user/' , views.create_patient_user, name='create-patient-user'),



]
