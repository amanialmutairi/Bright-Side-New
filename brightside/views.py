from django.shortcuts import render
from .models import patient, reseptionist, service

def index(request):
  return render(request, "brightside/index.html")