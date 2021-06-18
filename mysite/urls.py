from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('brightside/',include('brightside.urls')),    
    path('home/', Home,name="home"),  
    path('signup/',Sign_up,name="signup"), 
    path('signin/',Sign_in,name="signin"), 
]





