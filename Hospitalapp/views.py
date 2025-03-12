from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404

from Hospitalapp.models import *


# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def department(request):
    return render(request, 'departments.html')

def doctor(request):
    return render(request, 'doctors.html')

def appointment(request):
    if request.method == "POST":
        myappointments = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phonenumber=request.POST['phone'],
            datetime=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message']
        )
        myappointments.save()
        return redirect('/show')
    else:
        return render(request, 'appointment.html')

def show(request):
    all = Appointment.objects.all()
    return render(request,'show.html',{'all':all})

def delete(request,id):
  deleteappointment=Appointment.objects.get(id=id)
  deleteappointment.delete()
  return redirect('/show')

def edit(request,id):
    appointment=get_object_or_404(Appointment,id=id)
    if request.method == "POST":
        Appointment.name=request.POST.get('name')
        Appointment.email=request.POST.get('email')
        Appointment.phonenumber=request.POST.get('phonenumber')
        Appointment.datetime=request.POST.get('datetime')
        Appointment.department=request.POST.get('department')
        Appointment.doctor=request.POST.get('doctor')
        Appointment.message=request.POST.get('message')
        Appointment.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html',{'Appointment':appointment})

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('/Home')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')