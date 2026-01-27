# creación de constantes

habitaciones = {
    1: "Economica",
    2: "Estandar",
    3: "Superior",
    4: "Suite",
    5: "Presidencial"
}

valores = {
    1: 35000,
    2: 50000,
    3: 75000,
    4: 120000,
    5: 200000
}

# captura de tipo de habitación
print("Ingrese tipo de habitación (1 a 5):")

opcion_habitacion = int(input())

# captura de noches
print("ingrese cantidad de noches: ")
cantidad_noches = int(input())

if cantidad_noches > 0:
    
    match opcion_habitacion:
        case 1:
            costo_total = cantidad_noches * valores[opcion_habitacion]
            print("El tipo de habitación es: ", habitaciones[opcion_habitacion])
            print("El valor de la reserva es: ", costo_total)
        case 2:
            costo_total = cantidad_noches * valores[opcion_habitacion]
            print("El tipo de habitación es: ", habitaciones[opcion_habitacion])
            print("El valor de la reserva es: ", costo_total)
        case 3:
            costo_total = cantidad_noches * valores[opcion_habitacion]
            print("El tipo de habitación es: ", habitaciones[opcion_habitacion])
            print("El valor de la reserva es: ", costo_total)
        case 4:
            costo_total = cantidad_noches * valores[opcion_habitacion]
            print("El tipo de habitación es: ", habitaciones[opcion_habitacion])
            print("El valor de la reserva es: ", costo_total)
        case 5:
            costo_total = cantidad_noches * valores[opcion_habitacion]
            print("El tipo de habitación es: ", habitaciones[opcion_habitacion])
            print("El valor de la reserva es: ", costo_total)

else:
    print("Opción incorrecta. Debe ser un numero del 1 al 5")
