from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def home(request):
    data = TeamofDoctors.objects.all
    return render(request,"booking/home.html",{'data':data})

@login_required
def appointment_page(request,doctor_id):
    doctor = TeamofDoctors.objects.get(id=doctor_id)
    print(doctor)
    tokens = Token.objects.filter(doctor=doctor,is_booked=False)
    return render(request,"booking/appointment.html",{'doctor':doctor,'tokens':tokens})


@login_required
def book_appointment(request):
    if request.method == "POST":
        doctor_id = request.POST.get("doctor_id")
        mobile_no = request.POST.get("mobile_no")
        token_no = request.POST.get("token_id")

        print("Doctor ID:", doctor_id)
        print("Token Number:", token_no)

        try:
            token = Token.objects.get(doctor_id=doctor_id, token_number=int(token_no))
            print("Token:", token)
        except Token.DoesNotExist:
            messages.error(request, "Invalid token. Please select a valid token.")
            return redirect("appointment") 


        if token.is_booked:
            messages.error(request, "This token is already booked. Please choose another.")
            return redirect("appointment",token.doctor.id)

        appointment = Appointment.objects.create(
            user=request.user, contact_no=mobile_no, doctor=token.doctor, token=token
        )
        token.is_booked = True
        token.save()

        messages.success(request, "Booking Confirmed, Thank you!")
        return redirect("appointment", token.doctor.id)  

    return render(request, "booking/appointment.html")


def view_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request,"booking/my_appointments.html",{'appointments':appointments})

def cancel_appointment(request,doctor_id,token_no):
    token = Token.objects.get(doctor_id=doctor_id, token_number=token_no)
    token.is_booked=False
    token.save()

    appointment = Appointment.objects.get(doctor=doctor_id)
    appointment.delete()
    messages.success(request, "Booking Cancelled, Thank you!")
    return redirect("my_appointments")

def edit_appointment(request,doctor_id,token_no):
    doctor = TeamofDoctors.objects.get(id=doctor_id)
    tokens = Token.objects.filter(doctor_id=doctor_id,is_booked=False)
    appointment = Appointment.objects.get(doctor=doctor_id)
    return render(request,"booking/edit_appointment.html",{'doctor':doctor,'tokens':tokens,'appointment':appointment})


