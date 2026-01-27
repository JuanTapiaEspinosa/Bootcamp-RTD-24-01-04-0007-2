
print("Seleccione un producto:")
print("A.- Refresco")
print("B.- Papas fritas")
print("C.- Galletas")
producto = input("(A, B o C)").upper()

match producto:
    case "A": 
        print("Aquí tienes tu refresco")
    case "B":
        print("Aquí tienes tus papas fritas")
    case "C":
        print("Aquí tienes tus galletas")
    case _:
        print("Opción no reconocida")