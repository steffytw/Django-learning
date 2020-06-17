from django import forms
from . models import student,employeeData

class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','age','address','gender']



class studentDataForm(forms.Form):
    name = forms.CharField(label ='Name',required=True)
    age= forms.CharField(label='Age',widget=forms.NumberInput)
    address=forms.CharField(label='Address',widget=forms.Textarea)
    list1=[('Male','Male'),('Female','Female')]
    gender  = forms.ChoiceField(choices=list1,widget = forms.RadioSelect)


class FormValidation(forms.Form):
    name = forms.CharField(required=True)
    age= forms.CharField(widget=forms.NumberInput)
    address=forms.CharField(widget=forms.Textarea)
    list1=[('M','Male'),('F','Female')]
    gender  = forms.ChoiceField(choices=list1,widget = forms.RadioSelect)
    def clean_name(self):
        name1 = self.cleaned_data['name']
        if name1.isupper():
            raise forms.ValidationError('Name should be lowercase')
        return name1

class employeeForm(forms.Form):
    name = forms.CharField(label ='Name',required=True)
    age= forms.CharField(label='Age',widget=forms.NumberInput)
    emp_id=forms.CharField(label='Employee id',widget=forms.NumberInput)
    address=forms.CharField(label='Address',widget=forms.Textarea)
    upload_file=forms.FileField()

class employeeModelForm(forms.ModelForm):
    class Meta:
        model= employeeData
        fields = ['name','age','emp_id','address','upload_file']

class signupForm(forms.Form):
    firstname=forms.CharField(widget=forms.TextInput(),help_text='100 characters max.')
    lastname=forms.CharField(widget=forms.TextInput())
    username=forms.CharField(widget=forms.TextInput())
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    date_of_birth=forms.DateField()

    country_choice= [
        ('India', 'India'),
        ('Pakistan','Pakistan'),
        ('China', 'China'),
    ]
    country = forms.CharField(widget=forms.Select(choices=country_choice))

    
    address=forms.CharField(widget=forms.Textarea())

    password=forms.CharField(widget=forms.PasswordInput())
    confirmPassword=forms.CharField(widget=forms.PasswordInput())
    terms=forms.BooleanField()

    def clean_firstname(self):
        firstname=self.cleaned_data['firstname']
        if firstname.isupper():
            raise forms.ValidationError("please don't use uppercase")
        return firstname
    def clean_lastname(self):
        lname=self.cleaned_data['lastname']
        if lname.isupper():
            raise forms.ValidationError("please don't use uppercase")
        return lname
    
    def clean_confirmPassword(self):
        password = self.cleaned_data['password']
        confirmPassword=self.cleaned_data['confirmPassword']
        if not password == confirmPassword:
            raise forms.ValidationError("Password and Confirm password not match")
        return password

class MailSendingForm(forms.Form):
    subject=forms.CharField()
    message=forms.CharField()
    from_mail=forms.CharField()
    to_mail=forms.CharField()
    attachment=forms.FileField()



