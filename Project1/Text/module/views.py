from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'utilities/index.html')

def processed(request):
    if request.method == 'POST':
        
            FirstNumber=int(request.POST['FirstNumber'])
            SecondNumber=int(request.POST['SecondNumber']) #for storing data
            Result1= int(FirstNumber + SecondNumber)
            Result2= int(FirstNumber - SecondNumber)
            Result3= int(FirstNumber * SecondNumber)
            Result4= int(FirstNumber/SecondNumber)
            return render(request,'utilities/result.html', {'Result1' : Result1 , 'Result2': Result2 ,'Result3': Result3,'Result4': Result4})

       
        
    else:
        return HttpResponse("Request Method is Not POST")

        
    