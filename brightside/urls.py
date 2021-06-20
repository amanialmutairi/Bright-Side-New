from django.urls import path
from . import views


urlpatterns = [
  path('index/', views.index, name='index'),
  path('home/profile/<int:profile_id>/', views.user_profile, name='profile'),
  #path('register/', views.register, name='register'),
	path('login/', views.login_page, name="login"),  
	path('logout/', views.logout_user, name="logout"),
  path('request/', views.request_view, name='requests'),
  path('booking/', views.booking_admin, name='admin-booking'),
  path('calendar/', views.calendar, name='calendar'),
  path('forgot_password/', views.forgot_password, name='forgot_pass'),
  path('home/', views.booking_user, name='home'),
  path('index/count_appointment', views.count_appointment, name='count_apt'),
  path('index/count_patient', views.count_patient, name='count_patient'),
  path('index/total_earning', views.total_earning, name='total_earning'),
  path('delete/appointment/<int:apt_id>/', views.delete_appointment),



]
