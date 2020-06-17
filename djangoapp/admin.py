from django.contrib import admin
from . models import student,employeeData,Registration,Customer,College,Post

# Register your models here.

admin.site.register(student)
admin.site.register(employeeData)
admin.site.register(Registration)
admin.site.register(Customer)
admin.site.register(College)
admin.site.register(Post)

