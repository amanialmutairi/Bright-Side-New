from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .forms import ReseptionistForm, CreateUserForm
from .models import Patient, Reseptionist, Service, Appointment, Bill, Payment, Physician
from .decorators import unauthenticated_user, allowed_users
# Create your views here.
def index(request):
  return render(request, 'index.html')

#users
def user_profile(request):
  data = {}
  return render(request, 'user.html', context=data)

@unauthenticated_user
def register_page(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='patient')
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

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
#def index(request):
#	appointment = Appointment.objects.all()
#	patient = Patient.objects.all()
#	total_patient = Patient.count()
#	total_appointment = Appointment.count()
	#pending = Appointment.filter(status='Pending').count()

#	context = {'appointment':appointment, 'patient':patient,
#	'total_patient':total_patient,
#	'total_appointment':total_appointment  }



#	return render(request, 'index.html', context)

#requests
def request_view(request):
  return render(request, 'charts.html')

#view_calendar
def calendar(request):
  return render(request, 'cards.html')
#booking
def booking(request):
  return render(request, 'buttons.html')
#appointment

#reseptionist



#service

#Doctor

#bill

#payment