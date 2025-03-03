from django.contrib import admin
from Hospitalapp.models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctors)
admin.site.register(Staff)
admin.site.register(Ward)
admin.site.register(Appointment)