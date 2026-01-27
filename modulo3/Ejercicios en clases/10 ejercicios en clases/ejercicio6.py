
lugares = ["sala", "cocina", "sótano", "tesoro", "jardín"]

for posicion, lugar in enumerate(lugares):
    if lugar == "tesoro":
        print("Lo encontré en la posición ", posicion)
        break
