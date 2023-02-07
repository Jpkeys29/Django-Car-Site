from django.shortcuts import render,redirect
from django.urls import reverse
from . import models 


# Create your views here.

def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(request,'cars/list.html',context=context)
    #Also, context = {'all_cars':models.Car.objects.all()}


def add(request):
    #To check what it is being send on the form
    print(request.POST)
    #If statement for when the form is sent:
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
    #To create a new object:
        models.Car.objects.create(brand=brand, year=year)
    # if user submitted new car then go to list.html:
        return redirect(reverse('cars:list'))
    #initial return: return render(request,'cars/add.html')
    else: #if nothing has been POST
        return render(request,'cars/add.html')



def delete(request):
    return render(request,'cars/delete.html')
