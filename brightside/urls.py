from django.urls import path
from .views import index


urlpatterns = [
<<<<<<< HEAD
  path('index/', views.index, name='index'),
  path('user/profile', views.user_profile, name='profile'),
  path('register/', views.register_page, name='register'),
	path('login/', views.login_page, name="login"),  
	path('logout/', views.logout_user, name="logout"),
  path('request/', views.request_view, name='requests'),
  path('booking/', views.booking, name='booking'),
  path('calendar/', views.calendar, name='calendar'),
  path('forgot_password/', views.forgot_password, name='forgot_pass'),
  path('user/', views.user_page, name="user-page"),

=======
    path('home/', index)
>>>>>>> safaa_html/css
]
