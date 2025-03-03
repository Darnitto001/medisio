from django.shortcuts import render,redirect

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