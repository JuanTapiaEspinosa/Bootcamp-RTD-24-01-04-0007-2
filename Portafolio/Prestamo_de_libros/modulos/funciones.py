
# imports
import unicodedata
from .datos_basicos import libros, correos, usuarios_registrados

"""
Módulo: modulos.funciones
Descripción:
------------
Contiene funciones auxiliares utilizadas en el sistema de gestión de biblioteca.
Estas funciones se utilizan para:
- Normalizar títulos de libros eliminando mayúsculas y acentos.
- Generar un nuevo ID único para un libro.

Dependencias:
-------------
- unicodedata: Para normalizar caracteres Unicode y eliminar acentos.
- libros, correos, usuarios_registrados desde datos_basicos

Imports:
--------
import unicodedata
from .datos_basicos import libros, correos, usuarios_registrados
"""

# ======================================
# Funciones auxiliares
# ======================================


def normalizar_titulo(titulo):
    """
    Normaliza un título de libro para comparaciones consistentes.

    Parámetros:
    -----------
    titulo : str
        Título del libro que se desea normalizar.

    Retorno:
    --------
    str
        Título en minúsculas y sin acentos ni caracteres especiales.

    Ejemplo:
    --------
    >>> normalizar_titulo("Cien años de soledad")
    'cien anos de soledad'
    """
    titulo = titulo.lower()
    titulo = unicodedata.normalize("NFD", titulo)
    titulo = "".join(
        caracter for caracter in titulo if unicodedata.category(caracter) != "Mn")
    return titulo


def generar_nuevo_id():
    """
    Genera un nuevo ID único para un libro en el sistema.

    Comportamiento:
    ---------------
    - Si no existen libros en la lista 'libros', devuelve 1.
    - Si existen libros, devuelve el mayor ID existente más 1.

    Retorno:
    --------
    int
        Nuevo ID único para asignar a un libro.

    Ejemplo:
    --------
    >>> generar_nuevo_id()
    11   # si los libros existentes tienen IDs del 1 al 10
    """
    if not libros:
        return 1
    return max(libro["id"] for libro in libros) + 1
