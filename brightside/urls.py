from django.urls import path
from . import views


urlpatterns = [
  path('index', views.index, name='index'),
  path('user/profile', views.user_profile),
  path('register/', views.register_page, name="register"),
	path('login/', views.login_page, name="login"),  
	path('logout/', views.logout_user, name="logout"),
  path('request/', views.request_view, name='requests'),
  path('booking/', views.booking, name='booking'),
  path('calendar/', views.calendar, name='calendar'),


  #path('', views.index, name="index"),
  #path('user/', views.user_page, name="user-page"),
  #path('appointments/', views.appointment, name='appointments'),
  #path('patient/<str:pk_test>/', views.patient, name="patient"),

  #path('create_appointment/<str:pk>/', views.create_appointment, name="create_appointment"),
  #path('update_appointment/<str:pk>/', views.update_appointment, name="update_appointment"),
  #path('delete_appointment/<str:pk>/', views.delete_appointment, name="delete_appointment"),

]
