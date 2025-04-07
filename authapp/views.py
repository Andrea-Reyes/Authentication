from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegisterForm
from .encriptacion import cryptPassword
from .models import User
from django.http import HttpResponse
from django.contrib.auth import logout

def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email) 
                if user.password == cryptPassword(password):  
                    #messages.success(request, "¡Bienvenido!")

                    #Crear la sesión 'cookie' y agregar los datos
                    request.session['user_id'] = user.id
                    request.session['username'] = email
                    
                    #Agregar la durabilidad
                    request.session.set_expiry[3600]

                    #return redirect('dashboard')
                    return render(request,'dashboard.html')
                else:
                    #messages.error(request, "Datos incorrectos")
                    return render(request,'error.html')
            except User.DoesNotExist:
                messages.error(request, "Datos incorrectos")

    return render(request, 'login.html', {'form': form})

def register_view(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            role = form.cleaned_data.get("role", "user")

            if User.objects.filter(email=email).exists():
                messages.error(request, "El usuario ya está registrado")
                return render(request, 'register.html', {'form': form})

            encrypted_password = cryptPassword(password)
            User.objects.create(email=email, password=encrypted_password, role=role)

            return redirect('login')

    return render(request, 'register.html', {'form': form})

def dashboard_view(request):
    user_id = request.user_id
    usuario = request.usuario
    return HttpResponse(f'Bienvenido {usuario}, su ID es {user_id}')

    #Lo hicimos en clase
    #if 'user_id' in request.session:
    #    user_id = request.session["user_id"]
    #    usuario = request.session["username"]

    #    return HttpResponse(f'Bienvenido {usuario}, su ID es {user_id}')
    #else:
    #    return redirect('login')
    
    #Lo que tenía de primero
    #if request.user.is_authenticated:
    #    return render(request, 'dashboard.html')
    #else:
    #    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

def error_view(request):
    return render(request, 'error.html')