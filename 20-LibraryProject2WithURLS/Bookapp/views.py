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

from .forms import DepartmentForm, BookForm
from django.shortcuts import redirect
def AddNewDepartment(request):
    form = DepartmentForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('list_all_departments')
    
    
    return render(request, 'Bookapp/new_department.html', {'form':form})


def addNewBook(request, dept_id):
    dept = Department.objects.get(pk = dept_id)
    
    form = BookForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form = form.save(commit=False)
        form.dept = dept
        form.save()
        return redirect('display_department', dept_id = dept_id)
    
    
    
    return render(request,'Bookapp/AddnewBook.html',
                  {'Department': dept, 'form':form})
    
    
from .forms import MySignUpForm
from django.contrib.auth import login
def signmeUp(request):
    form = MySignUpForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        user = form.save()
        
        login(request, user)
        
        return redirect('list_all_departments')
    
    return render(request, 'Bookapp/Sign_up.html', {'form':form})
