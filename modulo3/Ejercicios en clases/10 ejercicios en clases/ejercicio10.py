vida_pikachu = 100
ataque_enemigo = 15
turno = 1
while vida_pikachu > 0:

    print("Turno ", turno, ":")
    print("¡Pikachu ha sido atacado!")
    vida_pikachu -= ataque_enemigo
    turno += 1
    if 20 > vida_pikachu > 0:
        print("¡Pikachu está en peligro!")
    elif vida_pikachu <= 0:
        print("¡Pikachu se ha debilitado!")
        break
