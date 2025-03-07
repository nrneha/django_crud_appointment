from django.shortcuts import render
from . models import *

def home(request):
    data = TeamofDoctors.objects.all
    return render(request,"booking/home.html",{'data':data})


def appointment_page(request,doctor_id):
    doctor = TeamofDoctors.objects.get(id=doctor_id)
    tokens = Token.objects.filter(doctor=doctor,is_booked=False)
    return render(request,"booking/appointment.html",{'doctor':doctor,'tokens':tokens})
