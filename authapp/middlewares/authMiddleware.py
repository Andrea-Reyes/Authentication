from django.shortcuts import redirect

class AuthMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        #Lista de rutas permitidas sin autenticación
        rutas_permitidas = ['/auth/login/','/auth/register/']

        #Verififcar si el usuario tiene la sesion activa
        user_id = request.session.get('user_id')

        if not user_id and request.path not in rutas_permitidas:
            return redirect('login')
        
        if user_id and request.path in rutas_permitidas:
            return redirect('dashboard')

        request.user_id = user_id
        request.usuario = request.sesion.get('username')

        response = self.get_response(request)
        return response