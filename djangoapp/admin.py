from django.contrib import admin
from . models import student,employeeData,Registration

# Register your models here.

admin.site.register(student)
admin.site.register(employeeData)
admin.site.register(Registration)

