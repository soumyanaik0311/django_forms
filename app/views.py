from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse
def djforms(request):
    ESTFO=StudentForm() #Empty student form object it is without any data
    d={'ESTFO':ESTFO}

    if request.method=='POST':
        SFDO=StudentForm(request.POST)  #student form object with data coming from frontend after post method is active
        # print(SFDO)
        if SFDO.is_valid():  #performing validation of fields
            return HttpResponse(str(SFDO.cleaned_data))

        else:
            return HttpResponse('Invalid Data')

    return render(request,'djforms.html',d)