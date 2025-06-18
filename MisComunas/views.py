from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Comuna
from .forms import ComunaForm

def listar_comunas(request):
    comunas = Comuna.objects.all()
    return render(request, 'list.html', {'comunas': comunas})

def crear_comuna(request):
    if request.method == 'POST':
        form = ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MisComunas:listar')
    else:
        form = ComunaForm()
    return render(request, 'form.html', {'form': form})

def editar_comuna(request, id):
    comuna = get_object_or_404(Comuna, pk=id)
    if request.method == 'POST':
        form = ComunaForm(request.POST, instance=comuna)
        if form.is_valid():
            form.save()
            return redirect('MisComunas:listar')
    else:
        form = ComunaForm(instance=comuna)
    return render(request, 'form.html', {'form': form})

def eliminar_comuna(request, id):
    comuna = get_object_or_404(Comuna, pk=id)
    if request.method == 'POST':
        comuna.delete()
        return redirect('MisComunas:listar')
    return render(request, 'confirm_delete.html', {'comuna': comuna})
    