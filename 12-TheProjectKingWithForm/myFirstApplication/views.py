from django.shortcuts import render
from .forms import Wow
# Create your views here.

def firstfunc(request):
    
    message = 'Hello fron frist application'
    
    form = Wow()
    
    if request.method == 'POST':
        form = Wow(request.POST)
        
        if form.is_valid():
            
            cd = form.cleaned_data
            message = cd['x']
    
    return render(request, 'myFirstApplication/firstpage.html',
                  {'form':form,'message': message})