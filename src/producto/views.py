from django.shortcuts import render
from .models import Producto
# Create your views here.
def listar_productos(request):
	productos = list(Producto.objects.all())
	return render(
        request,
        "productos/listado.html",
        {
            "titulo": "LISTADO DE ALUMNOS",
            "productos": productos,
        },
    )
def detalle_producto(request,pk):
	producto = get_object_or_404(Producto, id=pk)
	return render(
        request,
        "productos/detalle.html",
        {"titulo": f"{producto.nombre}", "producto":producto},
    )



def borrar_producto(request, pk):
    producto_a_borrar= get_object_or_404(Alumno, id=pk)
    producto_a_borrar.delete()

    return render(request, "productos/borrado.html")