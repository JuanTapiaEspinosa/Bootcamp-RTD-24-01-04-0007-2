"""
Módulo: datos_basicos.py
Descripción:
------------
Contiene las estructuras de datos iniciales del sistema de gestión de biblioteca.
Incluye libros, usuarios registrados, trabajadores y préstamos actuales.
También genera un conjunto de correos electrónicos de los usuarios registrados.

Estructuras de datos:
- libros: Lista de diccionarios con información de cada libro.
- prestamos: Lista de diccionarios con libros prestados y usuario asociado.
- trabajadores: Lista de diccionarios con credenciales de los trabajadores.
- usuarios_registrados: Lista de diccionarios con información de usuarios.
- correos: Conjunto de correos de los usuarios registrados (sin duplicados).
"""

# ======================================
# Lista de libros que existen actualmente en el sistema
# ======================================
libros = [
    {"id": 1, "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez", "año": 1967, "estado": "Disponible"},
    {"id": 2, "titulo": "Don quijote de la mancha",
        "autor": "Miguel de Cervantes", "año": 1605, "estado": "Prestado"},
    {"id": 3, "titulo": "1984", "autor": "George Orwell",
        "año": 1949, "estado": "Disponible"},
    {"id": 4, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry",
        "año": 1943, "estado": "Prestado"},
    {"id": 5, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury",
        "año": 1953, "estado": "Disponible"},
    {"id": 6, "titulo": "Crónica de una muerte anunciada",
        "autor": "Gabriel García Márquez", "año": 1981, "estado": "Disponible"},
    {"id": 7, "titulo": "La sombra del viento",
        "autor": "Carlos Ruiz Zafón", "año": 2001, "estado": "Prestado"},
    {"id": 8, "titulo": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling", "año": 1997, "estado": "Disponible"},
    {"id": 9, "titulo": "El código Da Vinci",
        "autor": "Dan Brown", "año": 2003, "estado": "Prestado"},
    {"id": 10, "titulo": "Matar a un ruiseñor",
        "autor": "Harper Lee", "año": 1960, "estado": "Disponible"}
]

# ======================================
# Registro de préstamos actuales
# ======================================
prestamos = [
    {'id': 2, 'titulo': 'Don quijote de la mancha', 'usuario': 'Ana Torres'},
    {'id': 4, 'titulo': 'El principito', 'usuario': 'Pablo Ramírez'},
    {'id': 7, 'titulo': 'La sombra del viento', 'usuario': 'Camila Fuentes'},
    {'id': 9, 'titulo': 'El código Da Vinci', 'usuario': 'Diego López'}
]

# ======================================
# Credenciales de trabajadores
# ======================================
trabajadores = [
    {"usuario": "admin", "password": "1234"},
    {"usuario": "ana", "password": "abcd"},
    {"usuario": "juan", "password": "pass123"}
]

# ======================================
# Lista de usuarios registrados
# ======================================
usuarios_registrados = [
    {"nombre": "Ana Torres", "rut": "12.345.678-5", "edad": 63,
        "telefono": 912345678, "correo": "ana.torres@email.com"},
    {"nombre": "Pablo Ramírez", "rut": "23.456.789-4", "edad": 16,
        "telefono": 923456789, "correo": "pablo.ramirez@email.com"},
    {"nombre": "Camila Fuentes", "rut": "34.567.890-1", "edad": 26,
        "telefono": 934567890, "correo": "camila.fuentes@email.com"},
    {"nombre": "Diego López", "rut": "45.678.901-2", "edad": 55,
        "telefono": 945678901, "correo": "diego.lopez@email.com"}
]

# ======================================
# Conjunto de correos de usuarios registrados
# ======================================
correos = set()
for usuario in usuarios_registrados:
    correos.add(usuario["correo"])

"""
Observaciones:
--------------
- Cada libro tiene un 'id' único, utilizado para identificarlo en préstamos.
- El campo 'estado' de los libros indica si está disponible o prestado.
- La lista 'prestamos' asocia libros con los usuarios que los tienen.
- La lista 'trabajadores' contiene las credenciales para el login del personal.
- El conjunto 'correos' asegura que no haya correos duplicados entre los usuarios.
"""
