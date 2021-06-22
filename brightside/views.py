
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import date
from django.db.models import Sum, Count, F



from .forms import  CreateUserForm, CreateAppointmentAdmin, CreateAppointmentUser, PatientForm
from .models import Patient, Reseptionist, Service, Appointment, Bill, Physician

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
    calc_earning = Appointment.objects.all().aggregate(total_earn= Sum('service__service_price'))
    
    context = {'count_appointments': appointments, 'count_patients': patients, 'total': calc_earning}

    return render(request, 'index.html', context)




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

def patient_list_view(request):
    data = {}
    data['patient'] = Patient.objects.filter(id=request.GET.get('search'))
    data['patient_list'] = Appointment.objects.filter(patient=request.GET.get('search'))
    return render(request, "searchbar.html", context = data)