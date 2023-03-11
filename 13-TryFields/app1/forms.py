from django import forms 

from datetime import datetime
class MyForm(forms.Form):
    
    levels = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth')
    )
    
    Departments = (
        ('CS', 'Computer Science'),
        ('IS', 'Information System'),
        ('IT', 'Information Technology'),
        ('AI', 'Artificial Intellegence'),
        ('IP', 'Image Processing'),
        ('MI', 'Medical Inormatics')
    )
    
    x = forms.IntegerField(label='Enter a Number' , max_value= 10, 
                           min_value=5, required= False)
    
    y = forms.CharField(label='Enter Text', max_length=5, min_length=3,
                        required= False)
    
    z = forms.BooleanField(label = 'Are you happy' , required= False)
    
    w = forms.ChoiceField(label='Select ', choices=levels, 
                          initial=(3, 'Third'))
    
    x2 = forms.DateField(label='Enter Your BirthDaya', initial= datetime.now ,
                         required=False)
    
    x3 = forms.DateTimeField(label='Enter Your BirthDaya', initial= datetime.now ,
                             required=False)
    """ 
    x4 = forms.DecimalField(label='Enter your GPA', decimal_places=2,
                            required=False)
    
    
    x4 = forms.FloatField(label='Enter your GPA', max_value= 70.55, min_value=10.55,
                            required=False)
     
     
    x4 = forms.DurationField(label='Enter Duaration: ',
                            required=False)
     
     
    x4 = forms.EmailField(label='Enter your email: ',
                            required=False)
     
    
    x4 = forms.URLField(label='Enter URL: ',
                            required=False)
                            
     
    x4 = forms.TimeField(label='Enter Time: ',initial=datetime.now,
                            required=False)
                           
     """
     
    x4 = forms.MultipleChoiceField(label='Select Prefered Departments: ', choices= Departments,
                            required=False)
    
     