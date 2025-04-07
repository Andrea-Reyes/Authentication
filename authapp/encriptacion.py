# encriptacion.py

def cryptPassword(password: str) -> str:
    """Invierte el string de la contraseña como método de 'encriptación'."""
    return password[::-1]

def validatePassword(input_password: str, stored_password: str) -> bool:
    """Valida si la contraseña ingresada coincide con la almacenada."""
    return cryptPassword(input_password) == stored_password
