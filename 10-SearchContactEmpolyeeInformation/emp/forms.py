from django import forms

class RegEmpForm(forms.Form):
    
    name = forms.CharField(label='NAme: ')
    salary = forms.FloatField(label='Salary: ')
    
    emp_email = forms.EmailField(label='Email: ')
    address = forms.CharField(label="Address: ")