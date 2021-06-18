from django.contrib import admin
from django.urls import path
from brightside.views import Home,SignUp,SignIn

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('home/', Home,name="home"),  
    path('signup/',SignUp,name="signup"), 
    path('signin/',SignIn,name="signin"), 
]





