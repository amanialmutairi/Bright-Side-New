
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import date
from django.db.models import Sum, Count, F
from .plots import line_plot, pie_plot, bar_plot
from django.contrib.auth.decorators import login_required

from .forms import  CreateUserForm, CreateAppointmentAdmin, CreateAppointmentUser, PatientForm, CreatPatientForm#, BillForm
from .models import Patient, Reseptionist, Service,Appointment, Bill, Physician

# Create your views here.


# users
#def forgot_password(request):
 #   return render(request, 'forgot-password.html')

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



#def login_page(request):

 #   if request.method == 'POST':
  #      username = request.POST.get('username')
   #     password = request.POST.get('password')

    #    user = authenticate(request, username=username, password=password)

     #   if user is not None:
      #      login(request, user)
       #     return redirect('index')
        #else:
         #   messages.info(request, 'Username OR password is incorrect')

    #context = {}
    #return render(request, 'login.html', context)


#def logout_user(request):
 #   logout(request)
  #  return redirect('login')


#receptionist dashboard
@login_required
def index(request):
    all_appointments = Appointment.objects.all()
    appointments = Appointment.objects.filter(appointment_date=date.today()).count()
    patients = Patient.objects.all().count()
    calc_earning = Appointment.objects.all().aggregate(total_earn= Sum('service__service_price'))
    prices = Appointment.objects.all()
    revenue = [x.service.service_price for x in prices]
    
    month = [x.appointment_date for x in prices]
    c = line_plot(revenue,month)
    
    context = {'daily_appointments': appointments, 'count_patients': patients, 'total': calc_earning,'all_appointments': all_appointments, 'chart': c }

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

def bill_view(request):
    data = {}
    data['bill'] = Bill.objects.all()
    #f = BillForm(request.POST or None, initial={'bill':patient.id})
    #data['from'] = f
    #if f.is_valid():
     # f.save()
    #return redirect('user-bill', id=id)
    return render(request, "bill.html", context=data)

def create_patient_account(request):
    f = CreatPatientForm(request.POST or None)
    data = {} 
    data['form'] = f
    if f.is_valid():
      f.save()
    return render(request, "create_patient.html", context=data)
