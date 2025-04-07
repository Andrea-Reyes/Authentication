from django.shortcuts import render
from .models import User
from django.db import models
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .encriptacion import validatePassword, cryptPassword

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email)
            if validatePassword(password, user.password):
                return JsonResponse({"message": "Login exitoso"})
            else:
                return JsonResponse({"error": "Contraseña incorrecta"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
    
    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role", "user")
        
        encrypted_password = cryptPassword(password)
        User.objects.create(email=email, password=encrypted_password, role=role)
        return JsonResponse({"message": "Registro exitoso"})
    
    return render(request, "register.html")
