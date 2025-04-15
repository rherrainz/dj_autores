from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Autor

# Create your views here.
def index(request):
    return render(request, 'frases/inicio.html')

@login_required
def autor_list(request):
    autores = Autor.objects.all().filter(activo=True)
    autores = sorted(autores, key=lambda x: (x.apellido, x.nombre))
    return render(request, 'frases/autores.html', {'autores': autores, 'estado': 'activos'})

@login_required
def inactivo_list(request):
    autores = Autor.objects.all().filter(activo=False)
    autores = sorted(autores, key=lambda x: (x.apellido, x.nombre))
    return render(request, 'frases/autores.html', {'autores': autores, 'estado': 'inactivos'})

@login_required
def autor_detail(request, autor_id):
    try:
        autor = Autor.objects.get(id=autor_id)
    except Autor.DoesNotExist:
        return render(request, 'frases/404.html', status=404)
    return render(request, 'frases/autor.html', {'autor': autor})

@login_required
def autor_json(request):
    autores = Autor.autores = Autor.objects.all().values('id', 'nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento', 'fecha_muerte', 'activo')
    return JsonResponse(list(autores), safe=False)

@login_required
def delete_autor(request, autor_id):
    try:
        autor = Autor.objects.get(id=autor_id)
        autor.delete()
        return JsonResponse({'message': 'Autor eliminado correctamente.'}, status=200)
    except Autor.DoesNotExist:
        return JsonResponse({'error': 'Autor no encontrado.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required    
def change_status(request, autor_id):
    try:
        autor = Autor.objects.get(id=autor_id)
        autor.activo = not autor.activo
        autor.save()
        return render(request, 'frases/autor.html', {'autor': autor})
    except Autor.DoesNotExist:
        return JsonResponse({'error': 'Autor no encontrado.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)