from django.contrib import admin
from django.urls import path
from us.views import Home,SignUp,Signin

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('home/', Home,name="home"),  
    path('signup/',SignUp,name="signup"), 
    path('signin/',Signin,name="signin"), 
]





