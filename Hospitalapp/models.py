from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Doctors(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Staff(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Position=models.CharField(max_length=100)
    Phonenumber=models.CharField(max_length=15)
    email=models.EmailField()
    hire_date=models.DateField()
    def __str__(self):
        return self.FirstName

class Ward(models.Model):
    Name=models.CharField(max_length=100)
    Totalbeds=models.IntegerField()
    Availablebeds=models.IntegerField()
    Returnname=models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class Appointment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=15)
    datetime=models.DateTimeField()
    department=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name

#mpesa Transactions
class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"