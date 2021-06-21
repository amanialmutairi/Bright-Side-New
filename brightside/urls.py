from django.urls import path
from . import views


urlpatterns = [
  path('index/', views.index, name='index'),
  path('home/profile/<int:profile_id>/', views.user_profile, name='profile'),
  path('home/profile/', views.profile_path, name='profile_path'),
  #path('register/', views.register, name='register'),
	path('login/', views.login_page, name="login"),  
	path('logout/', views.logout_user, name="logout"),
  path('delete/appointment/', views.manage_view, name='manage'),
  path('booking/', views.booking_admin, name='admin-booking'),
  path('calendar/', views.calendar, name='calendar'),
  path('forgot_password/', views.forgot_password, name='forgot_pass'),
  path('home/', views.booking_user, name='home'),
  path('index/count_appointment', views.count_appointment, name='count_apt'),
  path('index/count_patient', views.count_patient, name='count_patient'),
  path('index/total_earning', views.total_earning, name='total_earning'),
  path('delete/appointment/<int:apt_id>/', views.delete_appointment),
  path('patient/detail', views.dynamic_patient_view, name= 'patient-detail')



]
