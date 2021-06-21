
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import date




from .forms import  CreateUserForm, CreateAppointmentAdmin, CreateAppointmentUser, PatientForm
from .models import Patient, Reseptionist, Service, Appointment, Bill, Payment, Physician

# Create your views here.


# users
def forgot_password(request):
    return render(request, 'forgot-password.html')

def profile_path(request):
  return render(request,'profile.html')
  
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


#receptionist dashboard
def index(request):
    appointments = Appointment.objects.filter(appointment_date=date.today()).count()
    patients = Patient.objects.all().count()
    context = {'count_appointments': appointments, 'count_patients': patients}

    return render(request, 'index.html', context)


#def user_page(request):
 #   docs = Physician.objects.all()
  #  context = {'docs': docs}
   # return render(request, 'user_home.html', context)

# Manage Appointment Pathing
def manage_view(request):
    return render(request, 'manage_apt.html')

# view_calendar pathing
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

# User Booking
def booking_user(request):
    data = {}
    f = CreateAppointmentUser(request.POST or None)
    data["form"] = f
    if f.is_valid():
        f.save()
        return redirect("home")
    return render(request, 'user_home.html', context=data)





def total_earning(request):
  calc_earning = Appointment.objects.filter()
  data = {}
  total = sum[calc_earning.service_price]
  
  data['total'] = total
  return render(request, 'index.html', context=data)

def delete_appointment(request, apt_id):
  delete_apt = get_object_or_404(Appointment, id=apt_id)
  m = f"Do you want to delete {delete_apt.patient} appointment on {delete_apt.appointment_date} time: {delete_apt.appointment_time} with dr {delete_apt.physician}?"
  
  data={}
  data['message'] = m
  if "confirm" in request.GET:
    delete_apt.delete()
    return redirect('manage')
  elif 'cancel' in request.GET:
    return redirect('manage')
  return render(request, 'manage_apt.html', context=data)

def dynamic_patient_view(request):
    data = {}
    data['patient'] = Patient.objects.filter(id=request.GET.get('search'))
    data['patient_list'] = Appointment.objects.filter(patient=request.GET.get('search'))
    return render(request, "searchbar.html", context = data)