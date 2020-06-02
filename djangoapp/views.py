from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import student,employeeData,Registration
from . forms import studentForm,studentDataForm,FormValidation,employeeForm,signupForm,MailSendingForm
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage

# Create your views here.

# passing values from views to htmlpage

def homepage(request):
    course = 'Python'
    pythoninfo = ['inheritance', 'tuple', 'dictionary', 'list']
    return render(request, 'djangoapp/home.html', {'course1': course, 'pythoninfo1': pythoninfo})

#  inheriting layout in html
def layout(request):
    return render(request, 'djangoapp/layout.html')


def base(request):
    return render(request, 'djangoapp/base.html')

# fetching data from database
def studentData(request):
    students = student.objects.all()
    return render(request, 'djangoapp/students.html', {'students': students})

# switching between html pages
def studentDatalink(request):
    students = student.objects.all()
    return render(request, 'djangoapp/studentdata.html', {'students': students})


def studentDetails(request,id):
    students = student.objects.get(id=id)
    return render(request, 'djangoapp/studentdetails.html', {'students': students})

# crud operations: create read update and delete

def crudoperations(request):
    student1= student(name='lekshmi',age=25,address='kerala')  # create operation 1
    student1.save()
    return HttpResponse('saved to db..........')

    # student2= student()        # create operation 2
    # student2.name='Reeba'
    # student2.age = 34
    # student2.address='Kerala'
    # student2.save()
    # return HttpResponse('saved to db..........')

    # student3=student.objects.create(name='Zerah',age=22,address='UK')   # create operation 3
    # return HttpResponse('saved to db..........')


    # student4=student.objects.get(id=25)  # update operation
    # student4.name='Remya'
    # student4.age = 55
    # student4.save()
    # return HttpResponse('updated to db..........')

    # student5 = student.objects.get(id=25)      # delete operation
    # student5.delete()

    # return HttpResponse('Deleted from db..........')



#simple  model form

def modelform(request):
    form =studentForm()
    return render(request, 'djangoapp/modelform.html', {'form': form})

# model form validation

def modelformData(request):
    form =studentForm()
    if request.method == 'POST':
        form =studentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('data is saved to database......')
        else:
            return HttpResponse(form.errors)
    return render(request, 'djangoapp/model.html', {'form': form})

# normal form

def StudentFormData(request):
    form =studentDataForm()
    if request.method == 'POST':
        form =studentDataForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']

            s = student()

            s.name = name
            s.age = age
            s.address = address
            s.gender=gender
            s.save()
            return HttpResponse('data is saved to database......')
    return render(request, 'djangoapp/studentform.html', {'form': form})

# form validation

def validationFormData(request):
    form=FormValidation()
    if request.method == 'POST':
        form =FormValidation(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']

            s = student()

            s.name = name
            s.age = age
            s.address = address
            s.gender=gender
            s.save()
            return HttpResponse('data is saved to database......')

    return render(request, 'djangoapp/formvalidation.html', {'form': form})


# file upload

def  employee(request):
    if request.method=='POST':
        form=employeeForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            emp_id = form.cleaned_data['emp_id']
            upload_file = form.cleaned_data['upload_file']

            emp=employeeData()

            emp.name=name
            emp.age=age
            emp.address=address
            emp.emp_id=emp_id
            emp.upload_file=upload_file

            emp.save()
            return HttpResponse('data is saved to database......')
    else:
        form=employeeForm()
    return render(request, 'djangoapp/employee.html', {'form': form})



# signup form

def signup(request):
    form=signupForm()
    if request.method == 'POST':
        form =signupForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            country = form.cleaned_data['country']
            password = form.cleaned_data['password']
            confirmPassword = form.cleaned_data['confirmPassword']
            date_of_birth =form.cleaned_data['date_of_birth']
            

            register = Registration()

            register.firstname = firstname
            register.lastname = lastname
            register.username = username
            register.gender = gender
            register.address = address
            register.country = country
            register.password = password
            register.confirmPassword=confirmPassword
            register.date_of_birth = date_of_birth
            register.save()
            return HttpResponse('Form submitted!!')

    return render(request, 'djangoapp/signup.html', {'form': form})

def employeedetails(request):
    employees=employeeData.objects.all()
    return render(request, 'djangoapp/employeedetails.html', {'employees': employees})

# mail in console

def emailConsole(request):
    send_mail('subject','Hello world','abc@gmail.com',['to_mail'],fail_silently=False)
    return HttpResponse('Successfully send the mail')

#  mail sending with attachment

def MailSending(request):
    form=MailSendingForm
    if request.method=='POST':
        form=MailSendingForm(request.POST,request.FILES)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            from_mail=form.cleaned_data['from_mail']
            to_mail=form.cleaned_data['to_mail']
            attachment=form.cleaned_data['attachment']
            email=EmailMessage(subject,message,from_mail,[to_mail])
            email.attach(attachment.name,attachment.read(),attachment.content_type)
            email.send()
            return HttpResponse('Email send successfully  :).....!!!!!!')
    else:
        form=MailSendingForm()
    return render(request,'djangoapp/mailsend.html', {'form': form})

