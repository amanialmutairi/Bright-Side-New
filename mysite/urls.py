from django.contrib import admin
from django.urls import path
from brightside.views import Home,signup,signin

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('home/', Home,name="home"),  
    path('signup/',signup,name="signup"), 
    path('signin/',signin,name="signin"), 
]





