from django.urls import path
from . import views


urlpatterns = [
  path('index/', views.index, name='index'),
  path('user/profile', views.user_profile, name='profile'),
  path('register/', views.register, name='register'),
	path('login/', views.login_page, name="login"),  
	path('logout/', views.logout_user, name="logout"),
  path('request/', views.request_view, name='requests'),
  path('booking/', views.booking_admin, name='admin-booking'),
  path('calendar/', views.calendar, name='calendar'),
  path('forgot_password/', views.forgot_password, name='forgot_pass'),
  #path('home/', views.user_page, name='home'),
  path('home/', views.booking_user, name='home'),

]
