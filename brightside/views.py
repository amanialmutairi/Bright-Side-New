from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .forms import ReseptionistForm, CreateUserForm, CreateAppointment
from .models import Patient, Reseptionist, Service, Appointment, Bill, Payment, Physician
from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.
def indextest(request):
  return render(request, 'index.html')

#users
def forgot_password(request):
  return render(request, 'forgot-password.html')

  
def user_profile(request):
  return render(request, 'user.html')

@unauthenticated_user
def register_page(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='customer')
			user.groups.add(group)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		
		

	context = {'form':form}
	return render(request, 'register.html', context)

@unauthenticated_user
def login_page(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logout_user(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def index(request):
	appointment = Appointment.objects.all()
	patient = Patient.objects.all()
	#total_appointment = Appointment.count()
	

	context = {'appointment':appointment, 'patient':patient}
	#'total_appointment':total_appointment  

	return render(request, 'index.html', context)

def user_page(request):
	context = {}
	return render(request, 'userview.html', context)

#requests
def request_view(request):
  return render(request, 'charts.html')

#view_calendar
def calendar(request):
  return render(request, 'cards.html')
#booking
def booking(request):
  data = {}
  f = CreateAppointment(request.POST or None)
  data["form"] = f
  if f.is_valid():
    f.save()
    return redirect("booking") 
  return render(request, 'buttons.html', context=data )

#appointment

#reseptionist



#service

#Doctor

#bill

#payment