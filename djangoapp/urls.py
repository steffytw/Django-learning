from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('layout',views.layout),
    path('base',views.base),
    path('customer',views.CustomersDetails),
    path('studentinfo',views.studentData),
    path('studentlink',views.studentDatalink,name='studentDatalink'),
    path('studentDetails/<id>',views.studentDetails,name='studentDetails'),
    path('modelform',views.modelform),
    path('model',views.modelformData),
    path('form',views.StudentFormData),
    path('formval',views.validationFormData),
    path('crud',views.crudoperations),
    path('employee',views.employee),
    path('employeemodel',views.employeeModelFormData),
    path('signup',views.signup),
    path('employeedetails',views.employeedetails),
    path('email',views.emailConsole),
    path('mailsend',views.MailSending),
    path('setSession',views.setSession,name='setSession'),
    path('showSession',views.showSession,name='showSession'),
    path('login',views.login),
    path('college',views.CollegeData),
    path('page',views.index, name='index'),
    path('flower/<id>',views.PaginationData,name='PaginationData'),
    path('api/',views.ListStudent.as_view()),
    path('<int:pk>/',views.DetailStudent.as_view()),
       
]