from django.shortcuts import render

# Create your views here.
def secondfunc(request):
    
    return render(request, 'mySecondApplication/secondpage.html', 
                  {'message' : 'Hello From Second Application'})