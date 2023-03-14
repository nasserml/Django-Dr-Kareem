from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Department

def retriavedepartments(request):
    x = Department.objects.all()
    return render(request,'Bookapp/listalldepartment.html', {'departments' : x}) 

def deptDisplay(request, dept_id):
    dept = Department.objects.get(pk = dept_id)
    return render(request,'Bookapp/Department.html', {'Department': dept})

from .forms import DepartmentForm
from django.shortcuts import redirect
def AddNewDepartment(request):
    form = DepartmentForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('list_all_departments')
    
    
    return render(request, 'Bookapp/new_department.html', {'form':form})