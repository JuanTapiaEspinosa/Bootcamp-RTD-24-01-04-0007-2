experiencia = int(input("ingrese su experiencia (1 a 1000): "))
if experiencia < 100:
    print("Nivel 1: Novato")
elif 499 >= experiencia >= 100:
    print("Nivel 2: Intermedio")
elif experiencia >= 500:
    print("Nivel 3: Maestro")