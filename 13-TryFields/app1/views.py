from django.shortcuts import render

# Create your views here.
from .forms import MyForm
def startview(request):
    
    m = 'test'
    m1 = 'test1'
    m3 ='test'
    m4 = 'testt'
    m5 = 'test'
    m6 = 'test'
    m7 = 'test'
    form = MyForm()
    
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            m = cd['x']
            
            m1 = cd['y']
            
            m2 = cd['z']
            
            if m2 == True:
                m3 = 'since you are happy. give me $100'
            else:
                m3 = 'Sorry for being unhappy'
            
            m4 = cd['w']
            m5 = cd['x2']
            m6 = cd['x3']
            m7 = cd['x4']
        
    return render(request, 'mypage.html', {'form':form, 'output': m, 
                                           'output1' : m1
                                           ,'output2' : m3
                                           ,'output3' : m4
                                           ,'output4' : m5
                                           ,'output5' : m6
                                           ,'output6' : m7
                                           })
