
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import date
from django.db.models import Sum, Count, F
from .plots import line_plot, pie_plot, bar_plot
from django.contrib.auth.decorators import login_required


from .forms import  CreateUserForm, CreateAppointmentAdmin, CreateAppointmentUser, PatientForm
from .models import Patient, Reseptionist, Service,Appointment, Bill, Physician

# Create your views here.

# User-view pathing
def profile_path(request):
  return render(request,'profile.html')

# User-view user profile
def user_profile(request, profile_id):
    profile = get_object_or_404(Patient, profile_id=profile_id)
    f = PatientForm(request.POST or None, instance=profile)
    data = {}
    
    data['user_profile'] = Patient.objects.get(profile_id=profile_id)
    data['user_form'] = f

    if f.is_valid():
        form = f.save(commit=True)
        form.int = (form.p_first_name)
        form.save()
        return redirect('profile', profile_id=profile_id)
    return render(request, 'profile.html', context=data)


# User-view // user's appointments 
def user_appointment_view(request,pid):
    data = {}
    patient=Patient.objects.get(pk=pid)
    data['appiont'] =Appointment.objects.filter(patient=patient)
  
    return render(request, "user_appointments.html", context=data)


# User-view Create Account
def create_patient_user(request):
    f = CreateUserForm(request.POST or None)
    data = {} 
    data['form'] = f
    if f.is_valid():
      f.save()
      return redirect("home")
    return render(request, "create_account_user.html", context=data)

# User-view Booking
def booking_user(request):
    data = {}
    f = CreateAppointmentUser(request.POST or None)
    data["form"] = f
    if f.is_valid():
        f.save()
        return redirect("home")
    return render(request, 'user_home.html', context=data)

# Admin Dashboard
@login_required
def index(request):
    all_appointments = Appointment.objects.all()
    appointments = Appointment.objects.filter(appointment_date=date.today()).count()
    patients = Patient.objects.all().count()
    calc_earning = Appointment.objects.all().aggregate(total_earn= Sum('service__service_price'))

    prices = Appointment.objects.all().order_by("appointment_date")
    revenue = [x.service.service_price for x in prices]
    days = [x.appointment_date for x in prices ]

    print(f"days: {days}")
    print(f"rev: {revenue}")
    c = line_plot(days, revenue)
    
    context = {'daily_appointments': appointments, 'count_patients': patients, 'total': calc_earning,'all_appointments': all_appointments, 'chart': c }

    return render(request, 'index.html', context)




# Admin-view manage Appointment Pathing
def manage_view(request):
    return render(request, 'manage_apt.html')

# Admin-view Manage Appointment
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

# Admin-view all appointments  
def view_all_apt(request):
  data = {}
  data['all_appointments'] = Appointment.objects.all()
  return render(request, 'all_appointments.html', context = data)

# Admin-view Booking
def booking_admin(request):
    data = {}
    f = CreateAppointmentAdmin(request.POST or None)
    data["form"] = f
    if f.is_valid():
        f.save()
        return redirect("admin-booking")
    return render(request, 'booking.html', context=data)


# Admin-view user details
def patient_list_view(request):
    data = {}
    data['patient'] = Patient.objects.filter(profile_id=request.GET.get('search'))
    data['patient_list'] = Appointment.objects.filter(patient=request.GET.get('search'))
    return render(request, "searchbar.html", context = data)


# Admin-view create patient account
def create_patient_admin(request):
    f = CreateUserForm(request.POST or None)
    data = {} 
    data['form'] = f
    if f.is_valid():
      f.save()
    return render(request, "create_patient.html", context=data)


# Admin-view bills
def bill_detail(request):
    data = {}
    data['bill'] = Bill.objects.all()

    return render(request, 'bill.html', context=data)


# Admin-view unpaid bills   
def unpaid_filter(request):
  data={}
  bill = Bill.objects.filter(bill_status=1)
  data['unpaid'] = bill
  return render(request, "unpaid.html", context=data)


# Admin-view paid bills  
def paid_filter(request):
  data={}
  bill = Bill.objects.filter(bill_status=0)
  data['paid'] = bill
  return render(request, "paid.html", context=data)