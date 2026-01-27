numero = int(input("ingrese un numero máximo:"))

for num in range(1, numero + 1):
    if num % 2 == 0:
        print(num, "es un número par.")