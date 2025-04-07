# Clase: Funcionamiento de autenticación

Este proyecto es una aplicación de autenticación de usuarios en Django que permite el registro e inicio de sesión. Utiliza un modelo de usuario con los campos `email`, `password` y `role`. Además, emplea un sistema básico de encriptación donde la contraseña se almacena en orden inverso.

## Funcionalidades
- Registro de usuario con email, contraseña y rol.
- Inicio de sesión verificando email y contraseña.
- Encriptación básica de contraseñas invirtiendo el string.
- Validación de credenciales mediante comparación con la contraseña encriptada.

## Tarea
### Modificación de las vistas
Debes modificar las funciones de las vistas en `views.py` para:
1. Usar `forms` de Django en lugar de obtener los datos directamente desde `request.POST`.
2. Generar los formularios automáticamente en los templates utilizando los `forms` de Django en lugar del HTML manual.
3. Retornar templates en lugar de respuestas JSON:
   - Si el login es exitoso, redirigir a un `dashboard.html`.
   - Si hay un error en el login, mostrar un template `error.html` indicando el problema.
   - Si el registro es exitoso, redirigir a una página de bienvenida o al login.

## Archivos Clave
- `models.py`: Contiene el modelo de usuario.
- `views.py`: Contiene las funciones para login y registro.
- `encriptacion.py`: Contiene las funciones `validatePassword` y `cryptPassword`.
- `urls.py`: Configuración de rutas.
- `templates/`: Carpeta donde se encuentran los archivos HTML.

Creado para la clase de Programación Web 1 de la Universidad del Valle de Guatemala Campus Altiplano