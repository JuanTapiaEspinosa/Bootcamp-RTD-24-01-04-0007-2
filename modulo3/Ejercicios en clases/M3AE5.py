#Sistema de gestión de estudiantes
suma_total = 0
estudiantes = []
estudiante1 = ("Ana", 26, "Cordoba")
estudiantes.append(("Ana", 26, "Cordoba"))
estudiantes.append(("Luis", 19, "Valdivia"))
estudiantes.append(("Maria", 22, "Rancagua"))
estudiantes.append(("Pedro", 30, "Valparaiso"))
estudiantes.append(("Sofia", 22, "Valparaiso"))

#Recorrer la lista

for nombre, edad, ciudad in estudiantes:
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")


#Pedir ciudad y contar

ciudad_buscada = input("Ingresa una ciudad para buscar: ").strip()

contador = 0
for nombre, edad, ciudad in estudiantes:
    if ciudad.lower() == ciudad_buscada.lower():
        contador +=1
        
print(f"Estudiantes de {ciudad_buscada}: {contador}")

#Edad promedio

for estudiante in estudiantes:
    suma_total += estudiante[1]

edad_promedio = suma_total/len(estudiantes)
print(f"Suma total de edades = {suma_total}")
print(f"Promedio de edad = {edad_promedio}")