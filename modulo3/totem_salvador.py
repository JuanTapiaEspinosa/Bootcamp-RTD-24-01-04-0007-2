
import time
import sys

# ----- funciones -----

def mostrar_menu():

    print("=== BIENVENIDO AL HEALTH HUB DEL CESFAM ===")
    print("1. Solicitar Hora Médica")
    print("2. Urgencia Dental")
    print("3. Retirar Leche o Alimentos")
    print("4. Salir")
    print("**********************************")


# solicitar hora medica

def solicitar_hora_medica():
    print("=== BIENVENIDO A RESERVAS MEDICAS ===")
    print("**********************************")
    nombre = input("ingrese su nombre: ")
    print(f"Buscando disponibilidad para {nombre}...")
    time.sleep(2)
    print("Hora reservada con Dr. Pérez")
    print("**********************************")
    time.sleep(2)
    
# urgencia dental


def urgencia_dental():
    print("=== BIENVENIDO A URGENCIAS DENTALES ===")
    print("**********************************")
    nombre = input("ingrese su nombre: ")
    dolor = input("Presenta dolor agudo? (S/N): ").lower()
    time.sleep(2)

    if dolor == "s":
        
        print(">>> PASE DE URGENCIA GENERADO. Diríjase al Box 4 de inmediato.")
        time.sleep(2)
    else:
        print("No se detecta urgencia crítica. Por favor, pida una hora en medicina general.") 
        print("**********************************")
        time.sleep(2)
        


def retirar_leche_o_alimentos():
    print("=== BIENVENIDO A RETIRO DE ALIMENTOS ===")
    print("**********************************")
    rut = input("ingrese su rut (Ej: 12345678-9): ")
    print(f"Verificando beneficios para {rut}")
    time.sleep(2)
    print("Rut confirmado.")
    print("Entrega realizada con éxito.")
    print("**********************************")
    time.sleep(2)
    
def salir():
    print("Gracias que le vaya bien.")
    sys.exit()
    
# __name__ es una variable dunder, es decir una variable especial que python crea automaticamente al ejecutar este archivo
    
if __name__ == "__main__":
    
    # ----- Bloque principal -----

    opciones = {
        "1": solicitar_hora_medica,
        "2": urgencia_dental,
        "3": retirar_leche_o_alimentos,
        "4": salir
    }


    while True:
        
        mostrar_menu()
        opcion_menu = input("Seleccione una opción (1-4): ")
        
        if opcion_menu in opciones:
            funcion_a_ejecutar = opciones[opcion_menu]
            funcion_a_ejecutar()
        
    
