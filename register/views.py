from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect

from .models import Citizen,City,State
from .forms import FormCitizen,FormState,FormCity
from django.contrib import messages

# """Estas son las vistas de agregar Habitantes"""
def addcitizen(request):
    form=FormCitizen(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, f'El proceso fue realizado con éxito')
        return redirect('register:add')
    else:
        form=FormCitizen()
    citizen_list=Citizen.objects.all()
    return render(request,"register/add.html", {'citizen_list':citizen_list,'form':form,})


def editcitizen(request,citizen_id):
    citizen=get_object_or_404(Citizen,pk=citizen_id)
    form=FormCitizen(instance=citizen)
    citizen_list=Citizen.objects.all()
    return render(request,"register/add.html", {'citizen_list':citizen_list,'form':form,})


def deletecitizen(request,citizen_id):
    citizen=get_object_or_404(Citizen,pk=citizen_id)
    citizen.delete()
    messages.success(request, f'Usted eliminó a: {citizen.first_name} {citizen.last_name} {citizen.first_surnames}{citizen.last_surnames} con Cédula {citizen.cc}')
    return redirect('register:add')
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


#"""Estas son las vistas dpara Agregar, Eliminar y Editar Ciudades"""
def addspace(request):
    formcity=FormCity(request.POST)
    if formcity.is_valid():
        formcity.save()
        messages.success(request, f'El proceso fue realizado con éxito')
        return redirect('register:addspace')
    else:
        formcity=FormCity()

    formstate=FormState(request.POST)
    if formstate.is_valid():
        formstate.save()
        messages.success(request, f'Usted Acaba de agregar una ciudad con éxito')
        return redirect('register:addspace')
    else:
        formstate=FormState()
    
    city_list=City.objects.all()
    state_list=State.objects.all()
    return render(request,"register/space.html", {'city_list':city_list,'formcity':formcity,'formstate':formstate,'state_list':state_list,})


def editcity(request,city_id):
    city=get_object_or_404(Citizen,pk=city_id)
    formcity=FormCity(instance=city)
    formstate=FormState()
    city_list=City.objects.all()
    state_list=State.objects.all()
    return render(request,"register/space.html", {'city_list':city_list,'formcity':formcity,'formstate':formstate,'state_list':state_list,})


def deletecity(request,city_id):
    city=get_object_or_404(City,pk=city_id)
    city.delete()
    messages.success(request, f'Eliminó a: {city.city_name}')
    return redirect('register:addspace')
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#"""Estas son las vistas dpara Agregar, Eliminar y Editar Departamentos"""

def editstate(request,state_id):
    state=get_object_or_404(State,pk=state_id)
    formstate=FormState(instance=state)
    formcity=FormCity()
    state_list=State.objects.all()
    city_list=City.objects.all()
    return render(request,"register/space.html", {'city_list':city_list,'formcity':formcity,'formstate':formstate,'state_list':state_list,})


def deletestate(request,state_id):
    state=get_object_or_404(State,pk=state_id)
    state.delete()
    messages.success(request, f'Eliminó a: {state.state_name}')
    return redirect('register:addspace')
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""