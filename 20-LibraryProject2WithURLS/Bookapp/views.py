from django.shortcuts import render

# Create your views here.

from .models import Department

def retriavedepartments(request):
    x = Department.objects.all()
    return render(request,'Bookapp/listalldepartment.html', {'departments' : x}) 

def deptDisplay(request, dept_id):
    dept = Department.objects.get(pk = dept_id)
    return render(request,'Bookapp/Department.html', {'Department': dept})