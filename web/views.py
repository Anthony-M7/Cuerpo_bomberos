from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Usuarios

# Create your views here.

# Vista de la Ventana Inicial (Login)
def Home(request):
    # Condicional para ingresar al login si es TRUE  
    if request.method == "GET":
        return render(request, "index.html")
    # Condicional para consultar base de datos si es FALSE
    else:
      # Recibe el Usuario ingresado en el formulario
        usuario = request.POST["user"]
      # Recibe la contraseña ingresado en el formulario
        contrasena = request.POST["password"]
      # guarda los valores de la tabla que contiene a los usuarios
        users = Usuarios.objects.values()
        
        # Compara si el usuario y contraseña ingresados existen en la base de datos
        for user in users:
          # Si es True redirige al Dashboard
            if usuario == user["user"] and contrasena == user["password"]:
                return redirect("/dashboard/")
              
        # Si al verificar en todos los elementos no encuentra recarga el login
        return redirect("/")

# Vista de la ventana del Dashboard
def Dashboard(request):
    return render(request, "dashboard.html")