contraseña_secreta = "python123"

while 1 == 1:
    operador = input("ingrese contraseña: ")
    if operador == contraseña_secreta:
        print("Accesso concedido")
        break
    else:
        print("Contraseña incorrecta, intenta de nuevo.")
