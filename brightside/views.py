from django.shortcuts import render,redirect
from .forms import Signup
from django.contrib.auth import authenticate,logout,login

def SignUp(request):
    data=Signup(request.POST or None)
    if data.is_valid():
       data.save()
       return redirect("signin")
    
    context={
        'info':data,}
    return render(request,'signup.html',context)


def Home(request):
  return render(request,"home.html")


def SignIn(request):
    if request.method== 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")

    return render(request,'signin.html')