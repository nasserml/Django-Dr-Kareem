from django.shortcuts import render
from .forms import OneInt

def testview(request):
    
    m = ''
    
    sum = 0
    forms = []
    
    for i in range(1, 101):
        form = OneInt(prefix= 'form' + str(i), initial={'x' : i})
        forms.append(form)
    
    if request.method == 'POST':
        
        
        for i in range(1,101):
            form = OneInt(request.POST, prefix= 'form' + str(i))
            
            if form.is_valid():
                cd = form.cleaned_data
                x = cd['x']
                m += str(x) + ' + '
                sum += x
        m =m[:-2] + ' = '+str(sum)
            
    
    return render(request, 'test.html', {'forms':forms, 'output': m})