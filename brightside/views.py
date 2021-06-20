
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Physician
from datetime import date




from .forms import ReseptionistForm, CreateUserForm, CreateAppointmentAdmin, CreateAppointmentUser
from .forms import ReseptionistForm, CreateUserForm, PatientForm
from .models import Patient, Reseptionist, Service, Appointment, Bill, Payment, Physician

# Create your views here.


# users
def forgot_password(request):
    return render(request, 'forgot-password.html')


def user_profile(request, profile_id):
    profile = get_object_or_404(Patient, id=profile_id)
    f = PatientForm(request.POST or None, instance=profile)
    data = {}
    data['user_profile'] = Patient.objects.get(id=profile_id)
    data['user_form'] = f

    if f.is_valid():
        form = f.save(commit=True)
        form.int = (form.p_username)
        form.save()
        return redirect('profile', profile_id=profile_id)
    return render(request, 'profile.html', context=data)



#def register(request):
 # data = CreateUserForm(request.POST or None)
  #if data.is_valid():
   #    data.save()

 # return redirect('login')

  #context = {'info': data, }
  #return render(request, 'register.html', context)



def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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



def index(request):
    appointment = Appointment.objects.all()
    patient = Patient.objects.all()
    #total_appointment = Appointment.count()

    context = {'appointment': appointment, 'patient': patient}
    # 'total_appointment':total_appointment
    return render(request, 'index.html', context)


#def user_page(request):
 #   docs = Physician.objects.all()
  #  context = {'docs': docs}
   # return render(request, 'user_home.html', context)

# requests


def manage_view(request):
    return render(request, 'manage_apt.html')

# view_calendar


def calendar(request):
    return render(request, 'calendar.html')
# Admin Booking


def booking_admin(request):
    data = {}
    f = CreateAppointmentAdmin(request.POST or None)
    data["form"] = f
    if f.is_valid():
        f.save()
        return redirect("admin-booking")
    return render(request, 'booking.html', context=data)

# User booking_admin


def booking_user(request):
    data = {}
    f = CreateAppointmentUser(request.POST or None)
    data["form"] = f
    if f.is_valid():
        f.save()
        return redirect("home")
    return render(request, 'user_home.html', context=data)

def count_appointment(request):
  appointment = Appointment.objects.filter(appointment_date=date.today()).count()
  context={'appointment': appointment}
  return render(request, 'index.html', context)

def count_patient(request):
  patient = Patient.objects.all().count()
  data = {}
  data['patient'] = patient
  return render(request, 'index.html', context=data)

def total_earning(request):
  data = {}
  return render(request, 'index.html', context=data)

def delete_appointment(request, apt_id):
  delete_apt = get_object_or_404(Appointment, id=apt_id)
  m = f"Do you want to delete {delete_apt.patient} appointment on {delete_apt.appointment_date} time: {delete_apt.appointment_time}?"
  
  data={}
  data['message'] = m
  if "confirm" in request.GET:
    delete_apt.delete()
    return redirect('manage')
  elif 'cancel' in request.GET:
    return redirect('manage')
  return render(request, 'manage_apt.html', context=data)