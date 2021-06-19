
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import Physician


from .forms import ReseptionistForm, CreateUserForm, CreateAppointmentAdmin, CreateAppointmentUser
from .forms import ReseptionistForm, CreateUserForm, PatientForm
from .models import Patient, Reseptionist, Service, Appointment, Bill, Payment, Physician
from .decorators import unauthenticated_user, allowed_users, admin_only
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
        return redirect('profile', id=profile_id)
    return render(request, 'profile.html', context=data)


@unauthenticated_user
def register(request):

    data = CreateUserForm()
    if request.method == 'POST':
        data = CreateUserForm(request.POST or None)
        if data.is_valid():
            user = data.save()
            username = data.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'info': data, }
    return render(request, 'register.html', context)


@unauthenticated_user
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


@login_required(login_url='login')
@admin_only
def index(request):
    appointment = Appointment.objects.all()
    patient = Patient.objects.all()
    #total_appointment = Appointment.count()

    context = {'appointment': appointment, 'patient': patient}
    # 'total_appointment':total_appointment
    return render(request, 'index.html', context)


def user_page(request):
    docs = Physician.objects.all()
    context = {'docs': docs}
    return render(request, 'user_home.html', context)

# requests


def request_view(request):
    return render(request, 'requests.html')

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

# reseptionist


# service

# Doctor

# bill

# payment
