from django.shortcuts import render
from .models import Auto
from .forms import input_auto, BusquedaAuto
from django.http import HttpResponseRedirect


# Create your views here.

def inicio(request):
    return render(request, r'C:\Users\User\Desktop\CoderHouse\proyectofinal\miproyecto\templates\AppCoder\inicio.html',{} )

def categoria(request):
    return render(request, r'C:\Users\User\Desktop\CoderHouse\proyectofinal\miproyecto\templates\AppCoder\categoria.html' )

def equipo(request):
    return render(request, r'C:\Users\User\Desktop\CoderHouse\proyectofinal\miproyecto\templates\AppCoder\equipo.html' )


def auto(request):
    if request.method == 'POST':
        form = input_auto(request.POST)
        if form.is_valid():
            # process form data
            obj = Auto() #gets new object
            obj.marca = form.cleaned_data['marca']
            obj.chasis = form.cleaned_data['chasis']
            obj.tipo = form.cleaned_data['tipo']
            obj.motor = form.cleaned_data['motor']
            #finally save the object in db
            obj.save()
            return HttpResponseRedirect('/AppCoder')

    else:
        form = input_auto()

    return render(request, 'auto.html', {'form': form})


def busqueda_auto(request):


    auto_buscado = []
    dato = request.GET.get('partial_marca', None)
    
    if dato is not None:

        auto_buscado = Auto.objects.filter(marca__icontains = dato)
        print(auto_buscado)
        # return render(request, 'busqueda_auto.html', {'buscador': buscador, 'auto_buscado': auto_buscado})

    buscador = BusquedaAuto()

    return render(request, 'busqueda_auto.html', {'buscador': buscador, 'auto_buscado': auto_buscado})