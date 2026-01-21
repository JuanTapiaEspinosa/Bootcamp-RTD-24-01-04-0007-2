# imports

from .datos_basicos import libros, correos, usuarios_registrados, prestamos
from .funciones import normalizar_titulo, generar_nuevo_id



"""
Módulo: modulos.gestion_datos
Descripción:
------------
Contiene funciones para la gestión de libros y préstamos en el sistema de biblioteca.
Permite:
- Agregar y eliminar libros.
- Mostrar libros disponibles.
- Cambiar el estado de un libro (prestar o devolver).
- Registrar y eliminar préstamos.
- Buscar libros por título o ID.
- Buscar usuarios registrados por nombre.

Dependencias:
-------------
- libros, usuarios_registrados, prestamos, correos desde datos_basicos
- normalizar_titulo, generar_nuevo_id desde funciones


Imports:
--------
import unicodedata
from .datos_basicos import libros, correos, usuarios_registrados, prestamos
from .funciones import normalizar_titulo, generar_nuevo_id

"""

# ======================================
# Funciones de gestión de libros y préstamos
# ======================================


def agregar_libro_nuevo(titulo, autor, año):
    """
    Agrega un libro nuevo a la lista de libros existentes.

    Parámetros:
    -----------
    titulo : str
        Título del libro.
    autor : str
        Autor del libro.
    año : int
        Año de publicación.

    Retorno:
    --------
    str
        Mensaje de confirmación con el ID asignado al libro.
    """
    
    id_libro_nuevo = generar_nuevo_id()
    nuevo_libro = {
        "id": id_libro_nuevo,
        "titulo": titulo,
        "autor": autor,
        "año": año,
        "estado": "Disponible"
    }
    
    libros.append(nuevo_libro)
    return f'Libro: "{titulo}" agregado con ID {id_libro_nuevo}.'


def mostrar_libros_disponibles():
    """
    Muestra en pantalla todos los libros que están disponibles para préstamo.
    """
    hay_libros_disponibles = False
    for libro in libros:
        if libro["estado"] == "Disponible":
            print(f" {libro['titulo']} - {libro['estado']}")
            hay_libros_disponibles = True
    if not hay_libros_disponibles:
        print("No hay libros disponibles")


def cambiar_estado_libro(libro, accion, usuario):
    """
    Cambia el estado de un libro entre 'Disponible' y 'Prestado'.

    Parámetros:
    -----------
    libro : str
        Título del libro a prestar o devolver.
    accion : str
        'prestar' o 'devolver'.
    usuario : str
        Nombre del usuario que realiza la acción.

    Retorno:
    --------
    str
        Mensaje indicando el resultado de la acción.
    """
    libro = buscar_libro_por_titulo(libro)
    usuario = buscar_usuario_registrado(usuario)
    
    if libro is None:
        print("Libro no encontrado")
        return
    
    if usuario is None:
        print("Usuario no encontrado")
        return
    
    if accion == "prestar":
        if libro["estado"] == "Disponible":
            libro["estado"] = "Prestado"
            registrar_prestamo(libro, usuario)
            return f'"{libro["titulo"]}". El libro ha sido prestado correctamente a {usuario["nombre"]}.'
        else:
            return f'"{libro["titulo"]}" ya está prestado.'
    elif accion == "devolver":
        if libro["estado"] == "Prestado":
            libro["estado"] = "Disponible"
            eliminar_prestamo(libro)
            return f'"{libro["titulo"]}". El libro ha sido devuelto correctamente por {usuario["nombre"]}.'
        else:
            return f'"{libro["titulo"]}". El libro ya estaba disponible'
    else:
        return "Acción no válida"
    
def buscar_libro_por_titulo(titulo):
    """
    Busca un libro en la lista por su título.

    Parámetros:
    -----------
    titulo : str
        Título del libro a buscar.

    Retorno:
    --------
    dict | None
        Diccionario con los datos del libro si se encuentra, None si no.
    """
    titulo_usuario = normalizar_titulo(titulo)

    for libro in libros:
        titulo_libro = normalizar_titulo(libro["titulo"])
        if titulo_usuario == titulo_libro:
            return libro
    return None

def buscar_libro_por_id(id):
    """
    Busca un libro en la lista por su ID.

    Parámetros:
    -----------
    id : int
        ID del libro a buscar.

    Retorno:
    --------
    dict | None
        Diccionario con los datos del libro si se encuentra, None si no.
    """
    id = int(id)
    
    for libro in libros:
        if libro["id"] == id:
            return libro
    return None
    

def eliminar_libro(id):
    """
    Elimina un libro de la lista de libros existentes.

    Parámetros:
    -----------
    id : int
        ID del libro a eliminar.

    Retorno:
    --------
    str
        Mensaje indicando si se eliminó correctamente o si no se encontró el libro.
    """
    libro = buscar_libro_por_id(id)
    
    if libro is None:
        return "No se encontró ningún libro con ese ID"
    
    
    libros.remove(libro)
    return f'Libro "{libro["titulo"]}" eliminado correctamente'
    
    print("")
    
def buscar_usuario_registrado(usuario_buscado):
    """
    Busca un usuario en la lista de usuarios registrados por nombre.

    Parámetros:
    -----------
    usuario_buscado : str
        Nombre del usuario a buscar.

    Retorno:
    --------
    dict | None
        Diccionario con los datos del usuario si se encuentra, None si no.
    """
    
    usuario_buscado = normalizar_titulo(usuario_buscado)
    
    for u in usuarios_registrados:
        u_nombre = normalizar_titulo(u["nombre"])
        if u_nombre == usuario_buscado:
            return u
    return None
    
    
def registrar_prestamo(libro, usuario):
    """
    Registra un nuevo préstamo en la lista de préstamos existentes.

    Parámetros:
    -----------
    libro : dict
        Diccionario con los datos del libro a prestar.
    usuario : dict
        Diccionario con los datos del usuario que recibe el libro.
    """
    nuevo_prestamo = {
        "id": libro["id"],
        "titulo": libro["titulo"],
        "usuario": usuario["nombre"]
    }
    prestamos.append(nuevo_prestamo)
    
def eliminar_prestamo(libro):
    """
    Elimina un préstamo de la lista de préstamos existentes basado en el título del libro.

    Parámetros:
    -----------
    libro : dict
        Diccionario con los datos del libro que se devuelve.
    """
    for p in prestamos:
        if p["titulo"] == libro["titulo"]:
            prestamos.remove(p)
    
    






 





























