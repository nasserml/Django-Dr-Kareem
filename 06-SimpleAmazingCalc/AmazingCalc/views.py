from django.shortcuts import render
from .forms import OneInt

def testview(request):
    
    x = 0
    form = OneInt()
    
    if request.method == 'POST':
        form = OneInt(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            x = cd['x']
    
    return render(request, 'test.html', {'form':form, 'output': x})