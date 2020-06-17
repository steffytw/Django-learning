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

class Customer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    class Meta:
        verbose_name_plural ="Customer Details"
    def __str__(self):
        return self.name

class College(models.Model):
    MEDIA_CHOICES = [
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),

    ]
    media = models.CharField(
            max_length=10,
            choices=MEDIA_CHOICES,
            default='Audio',

        )
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
    class Meta:
        verbose_name_plural ="College"
    def __str__(self):
        return self.year_in_school

class Post(models.Model):
    title = models.CharField(max_length=255,default='',blank=True)
    description = models.TextField()
    class Meta:
        verbose_name_plural ="Flowers"
    def __str__(self):
        return self.title


    