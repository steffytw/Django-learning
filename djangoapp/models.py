from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    gender=models.CharField(max_length=10,default="NA")
    
    class Meta:
        verbose_name_plural ="student details"
    def __str__(self):
        return self.name

class employeeData(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address= models.TextField()
    emp_id=models.IntegerField()
    upload_file=models.FileField(upload_to="documents")
    class Meta:
        verbose_name_plural ="Employee Details"
    def __str__(self):
        return self.name

class Registration(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    country=models.CharField(max_length=50)
    address=models.TextField()
    password=models.CharField(max_length=50)
    class Meta:
        verbose_name_plural ="Registration Details"
    def __str__(self):
        return self.username
