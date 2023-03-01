from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def hello_world(request):
    return HttpResponse('''
                        
    <h1 style="background-color: aquamarine; color:brown; border: 4px solid black; margin: 15px; text-align: center; width:: 300px ;">
    Hello from Django
</h1>
                        
                        ''')
    
    
@csrf_exempt
def addxy(request):
    if(request.method == 'POST'):
        
        x = int(request.POST.get('firstvalue'))
        y = int(request.POST.get('secondvalue'))
        
        z = x + y
        return HttpResponse("Result = " + str(z))

    else:
        return HttpResponse('''
                            
                            <form action="addtwonumbers" method="POST">
        <p>
            <label for="firstvalue"> Enter First Number</label>
            <input type="text" name="firstvalue"/>
        </p>

        <p>
            <label for="secondvalue"> Enter Second Number</label>
            <input type="text" name="secondvalue"/>
        </p>

        <button type="submit">ADD</button>

    </form>
                            ''')
