# imports

import modulos
import time
import sys
# ========================================
# Inicio de sesión para trabajadores
# ========================================


"""
Solicita al usuario sus credenciales y valida el acceso.

Parámetros:

-----
intentos: int
    Cantidad de intentos restantes para ingresar las credenciales. Default: 3
    
Funcionamiento:

------------
1. Solicita usuario y contraseña por consola
2. Valida las credenciales usando modulos.validaciones.validar_credenciales().
3. Si son correctas, muestra mensaje de bienvenida.
4. Si son incorrectas, disminuye los intentos y vuelve a llamar recursivamente la función.
5. Si los intentos llegan a 0, bloquea el acceso

Devuelve:
------------
None
"""

def login(intentos=3):
    if intentos == 0:
        print("Acceso bloqueado")
        sys.exit()

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    if modulos.validaciones.validar_credenciales(usuario, password):
        print(f"Bienvenido, {usuario}")
        return
    else:
        print(f"Datos incorrectos. Intentos restantes: {intentos - 1}")
        login(intentos - 1)
# ========================================
# Menú principal
# ========================================

# Muestra las opciones disponibles del menú principal
def menu_principal():

    print(" ---- Bienvenido a bibliotECAS ----")
    print(" 1.- Ver libros disponibles ")
    print(" 2.- Buscar libro")
    print(" 3.- Prestar libro")
    print(" 4.- Devolver libro")
    print(" 5.- Agregar libro nuevo")
    print(" 6.- Eliminar libro")
    print(" 0.- Salir")
    print(" -----------------------------------")
    
# ========================================
# Funciones de menú
# ========================================
    
# Muestra todos los libros disponibles
def opcion_mostrar_libros_disponibles():
    modulos.gestion_datos.mostrar_libros_disponibles()

# Solicita el título del libro y nombre del usuario
# Muestra la información si el libro existe, o un mensaje si no lo encuentra.
def opcion_buscar_libro_titulo():
    titulo = input(" Por favor ingrese titulo del libro: ")
    libro_buscado = modulos.gestion_datos.buscar_libro_por_titulo(titulo)
    if libro_buscado is None:
        print(" ---- Libro no encontrado ---- ")
        return
    else:
        print(" ----Libro encontrado con éxito----")
        print(f"Titulo:  {libro_buscado['titulo']}")
        print(f"estado:  {libro_buscado['estado']}")

# Solicita el título del libro y nombre del usuario
# Cambia el estado del libro a "Prestado" y registra el préstamo
def opcion_prestar_libro():
    titulo = input(" Por favor ingrese titulo del libro a prestar: ")
    usuario = input(" Por favor ingrese el nombre del usuario: ")
    accion = "prestar"
    mensaje = modulos.gestion_datos.cambiar_estado_libro(titulo, accion, usuario)
    if mensaje is not None:
        print(mensaje)

# Solicita el título del libro y nombre del usuario
# Cambia el estado del libro a "Disponible" y elimina el registro del préstamo
def opcion_devolver_libro():
    titulo = input(" Por favor ingrese titulo del libro a devolver: ")
    usuario = input(" Por favor ingrese el nombre del usuario ")
    accion = "devolver"
    mensaje = modulos.gestion_datos.cambiar_estado_libro(titulo, accion, usuario)
    if mensaje is not None:
        print(mensaje)
    
# Solicita información de un libro nuevo y lo agrega a la lista de libros
def opcion_agregar_libro_nuevo():
    
    titulo = input(" Ingrese titulo : ")
    autor = input(" Ingrese autor : ")
    año = input(" Ingrese año de publicación : ")
    
    mensaje1 = modulos.gestion_datos.agregar_libro_nuevo(titulo, autor, año)
    
    print(" ", mensaje1)
    
# Solicita ID del libro y lo elimina de la lista de libros 
def opcion_eliminar_libro():
    
    id = input(" Ingrese el ID del libro a eliminar: ")
    mensaje = modulos.gestion_datos.eliminar_libro(id)
    print(mensaje)

# Cierra el programa
def opcion_salir():
    print(" Gracias por utilizar bibliot-ECAS ")
    sys.exit()

# ========================================
# Diccionario de opciones del menú
# ========================================
opciones = {
    "1":opcion_mostrar_libros_disponibles,
    "2":opcion_buscar_libro_titulo,
    "3":opcion_prestar_libro,
    "4":opcion_devolver_libro,
    "5":opcion_agregar_libro_nuevo,
    "6":opcion_eliminar_libro,
    "0":opcion_salir
}

# ========================================
# Inicio del programa
# ========================================


login() #Función recursiva



while True:

    menu_principal()
    opcion_menu = input(" Por favor seleccione una opción (0-6): ")
    time.sleep(1)
    
    
    if opcion_menu in opciones:
        funcion_a_ejecutar = opciones[opcion_menu]
        funcion_a_ejecutar()
        print(" -----------------------------------")
        time.sleep(1)
    else:
        print(" Ingrese una opción valida ")
        print(" -----------------------------------")
        time.sleep(1)


"""
1.-mostrar solo libros disponibles
2.-mostrar solo libros disponibles
3.-buscar libro por título
4.-prestar libro
5.-devolver libro
6.-agregar libro nuevo
7.-eliminar libro
0.-salir
"""
