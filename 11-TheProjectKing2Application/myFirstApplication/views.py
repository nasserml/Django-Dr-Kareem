from django.shortcuts import render

# Create your views here.

def firstfunc(request):
    return render(request, 'myFirstApplication/firstpage.html',
                  {'message': 'Hello fron frist application'})