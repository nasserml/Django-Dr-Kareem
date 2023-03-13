from django.shortcuts import render

# Create your views here.

from .models import Department

def retriavedepartments(request):
    x = Department.objects.all()
    return render(request,'Bookapp/listalldepartment.html', {'departments' : x}) 