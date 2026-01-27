edad = int(input("ingrese edad: "))
identificacion = input("¿traes identificación? (S/N): ")

if edad >= 18 and identificacion.upper() == "S":
    print("Adelante disfrute la fiesta.")
    
else: 
    print("Lo siento, no puedes entrar a la fiesta.")
 
    