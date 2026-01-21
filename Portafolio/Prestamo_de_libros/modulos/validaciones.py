"""
Módulo: modulos.validaciones.py
Descripción:
------------
Contiene funciones de validación utilizadas en el sistema de gestión de biblioteca.
Incluye validación de:
- Correos electrónicos
- Credenciales de trabajadores
- Estado de préstamos de libros
- Existencia de usuarios registrados

Dependencias:
-------------
- libros, correos, usuarios_registrados, trabajadores, prestamos desde datos_basicos
- funciones (módulo auxiliar)
"""

from .datos_basicos import libros, correos, usuarios_registrados, trabajadores, prestamos

# ======================================
# Funciones de validación
# ======================================

def verificar_correo(nuevo_correo):
    """
    Valida la estructura de un correo electrónico y verifica si ya está registrado.

    Parámetros:
    -----------
    nuevo_correo : str
        Correo electrónico a validar.

    Comportamiento:
    ---------------
    1. Verifica que el correo contenga exactamente un '@' y ambas partes no estén vacías.
    2. Comprueba si el correo ya existe en el conjunto 'correos'.
    3. Imprime mensajes informativos dependiendo del resultado de la validación.
    """
    partes = nuevo_correo.split("@")

    if len(partes) == 2 and all(partes):
        if nuevo_correo in correos:
            print(f"El correo '{nuevo_correo}' ya está en uso")
        else:
            print(f"El correo '{nuevo_correo}' ha sido registrado con éxito")
    else:
        print("Correo inválido")


def validar_credenciales(usuario, password):
    """
    Valida las credenciales de un trabajador.

    Parámetros:
    -----------
    usuario : str
        Nombre de usuario del trabajador.
    password : str
        Contraseña asociada al usuario.

    Retorno:
    --------
    bool
        True si las credenciales coinciden con algún trabajador registrado.
        False en caso contrario.
    """
    for trabajador in trabajadores:
        if trabajador["usuario"] == usuario and trabajador["password"] == password:
            return True
    return False


def validar_libro_prestado(titulo):
    """
    Verifica si un libro está actualmente prestado.

    Parámetros:
    -----------
    titulo : str
        Título del libro a verificar.

    Retorno:
    --------
    bool
        True si el libro ya está prestado (existe en la lista 'prestamos').
        False si el libro está disponible.
    """
    for p in prestamos:
        if p["titulo"] == titulo:
            return True
    return False


def validar_usuario(usuario_buscado):
    """
    Verifica si un usuario registrado existe en el sistema.

    Parámetros:
    -----------
    usuario_buscado : str
        Nombre del usuario a verificar.

    Retorno:
    --------
    bool
        True si el usuario existe en 'usuarios_registrados'.
        False si no existe.
    """
    for u in usuarios_registrados:
        if u["nombre"] == usuario_buscado:
            return True
    return False
