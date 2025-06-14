from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Comuna
from .forms import ComunaForm

def listar_comunas(request):
    """Vista para listar todas las comunas"""
    try:
        comunas = Comuna.objects.all().order_by('nombre')
        return render(request, 'MisComunas/list.html', {'comunas': comunas})
    except Exception as e:
        messages.error(request, f"Error al obtener las comunas: {str(e)}")
        return render(request, 'MisComunas/list.html', {'comunas': []})

def crear_comuna(request):
    """Vista para crear una nueva comuna"""
    if request.method == 'POST':
        form = ComunaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Comuna creada exitosamente!")
                return redirect('MisComunas:listar')  # Usando namespace
            except Exception as e:
                messages.error(request, f"Error al guardar la comuna: {str(e)}")
        else:
            messages.warning(request, "Por favor corrige los errores en el formulario")
    else:
        form = ComunaForm()
    
    return render(request, 'MisComunas/form.html', {
        'form': form,
        'accion': 'Crear'
    })

def editar_comuna(request, id):
    """Vista para editar una comuna existente"""
    comuna = get_object_or_404(Comuna, id=id)
    
    if request.method == 'POST':
        form = ComunaForm(request.POST, instance=comuna)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Comuna actualizada exitosamente!")
                return redirect('MisComunas:listar')  # Usando namespace
            except Exception as e:
                messages.error(request, f"Error al actualizar la comuna: {str(e)}")
        else:
            messages.warning(request, "Por favor corrige los errores en el formulario")
    else:
        form = ComunaForm(instance=comuna)
    
    return render(request, 'MisComunas/form.html', {
        'form': form,
        'accion': 'Editar',
        'comuna': comuna
    })

def eliminar_comuna(request, id):
    """Vista para eliminar una comuna"""
    comuna = get_object_or_404(Comuna, id=id)
    
    if request.method == 'POST':
        try:
            comuna.delete()
            messages.success(request, "Comuna eliminada exitosamente!")
            return redirect('MisComunas:listar')  # Usando namespace
        except Exception as e:
            messages.error(request, f"Error al eliminar la comuna: {str(e)}")
            return redirect('MisComunas:listar')
    
    return render(request, 'MisComunas/confirm_delete.html', {
        'comuna': comuna
    })
    