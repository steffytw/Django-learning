# Django
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It's free and open source. 

# Django Installation and project creation:

- Step 1 Download [Python](https://www.python.org/downloads/)
- Step 2 Install pip



```
  	sudo apt install python-pip
	
```



    
- Step 3  Create a folder for django project
- Step 4  Create a virtual environment



```
  	pip install virtualenv
        python -m virtualenv nameofthevirtualenv
	
```

- Step 5  Activate the virtual environment


linux:

```
	source nameofthevirtualenv/bin/activate

```
windows:

```
	nameofthevirtualenv\Scripts\activate

```
- Step 6  Install Django


```
  	pip install django
	
```


- Step 7  Create django project

for example, project name as djangoProject1

```
  	django-admin startproject djangoProject1 .
	
```


# Django app creation steps:
- Step 1  Create django app 

for example app name as djangoapp
```
python manage.py startapp djangoapp
```
- Step 2  Go to settings.py file in the djangoProject1 folder and update the installed apps with the created app name.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoapp',
]

```
- Step 3 After this go to urls.py file in the djangoProject1 folder

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/',include('djangoapp.urls')),
]
```
- Step 4 Create a urls.py file in the djangoapp.

```
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name = 'home'),
]
```

- Step 5 create a view in the view.py file 


```
# Create your views here.

def home(request):
	return HttpResponse('HELLO WORLD')

```
# Migrations

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.


```
python manage.py makemigrations
python manage.py migrate

```

# Run an app :
To run a Django app on localhost

  python 2:

```
  	python manage.py runserve
	
```

   python 3:
```
  	python3 manage.py runserve
	
```
# File Uploading in Django  :
- Step 1 Create a model in models.py

```

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
```
- Step 2 To upload the file in html ,create a form in forms.py

```
from django import forms
from . models import employeeData
class employeeModelForm(forms.ModelForm):
    class Meta:
        model= employeeData
        fields = ['name','age','emp_id','address','upload_file']

```
- Step 3 To handle the uploaded file ,go to views.py

```
from django.shortcuts import render
from django.http import HttpResponse
from . models import employeeData
from . forms import employeeModelForm

def employeeModelFormData(request):
    form =employeeModelForm()
    if request.method == 'POST':
        form =employeeModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('data is saved to database......')
        else:
            return HttpResponse(form.errors)
    return render(request, 'djangoapp/empmodel.html', {'form': form})

```
- Step 4 To upload the file in html , add the enctype in form 

```
<form action="" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
        <table>
            {{form}}
        </table>
        <button class="btn btn-priar" type="submit">Submit</button>
   </form>

```
- Step 5 For uploading the file, add MEDIA_ROOT and MEDIA_URL in settings.py of the project folder

```
MEDIA_ROOT = os.path.join(BASE_DIR,'Media')
MEDIA_URL = '/media/'


```


# Django REST API :

Django Rest API  is an application used for rapidly building RESTful APIs based on Django models.


- Step 1 Install djangorestframework

```
pip install djangorestframework
```

- Step 2 Go to settings.py in the django project folder and add 'rest_framework' in INSTALLED_APPS .

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoapp',
    'rest_framework',

]
```
- Step 3 Create a class in models.py in app folder

```
from django.db import models
    class Student (models.Model):
        name = models.CharField(max_length = 20)
        address = models.TextField()

    def __str__(self):
        return self.name
```
- Step 4 Register the model in admin.py inside the app folder
```
from django.contrib import admin
    from .models import Student
    
    admin.site.register(Student)
```
- Step 5 Create a new file serializers.py inside the app folder
```
 
    from rest_framework import serializers
    from .import models
    class StudentSerializer(serializers.ModelSerializer):
        class Meta:
            fields = ('id','name','address')
            model = models.Student
```
- Step 6 Go to views.py in app folder 
```
    from django.shortcuts impport render
    from rest_framework import generics
    from .models import Student
    from .import serializers
    
    class ListStudent(generics.ListCreateAPIView):
        queryset = Student.objects.all()
        serializer_class = serializers.StudentSerializer

    class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
        queryset = Student.objects.all()
        serializer_class = serializers.StudentSerializer
```
- Step 7 Update urls.py in app folder
```
    from django.urls import path
    from .import views
    urlpatterns = [
        path('api/',views.ListStudent.as_view()),
        path('<int:pk>/',views.DetailStudent.as_view())
    ]
```
- Step 8  Check the output

    - Listview is at http://127.0.0.1:8000/api/
    - DetailView is at http://127.0.0.1:8000/2/
