from modulos import Departamento, Edificio, Administracion


from modulos import Departamento, Edificio

# Crear objetos Departamento
departamento1 = Departamento(301, "Valentina Rojas", 65, 42000)
departamento2 = Departamento(402, "Sebastián Fuentes", 72, 38000)
departamento3 = Departamento(503, "Camila Sánchez", 88, 56000)

# Crear objeto Edificio
edificio_santa_isabel = Edificio(
    nombre="Edificio Santa Isabel",
    direccion="Calle Santa Isabel 1450, Santiago",
    nombre_administrador="Don Ricardo Muñoz",
    telefono_administrador="+56 9 8765 4321"
)

# Agregar departamentos al edificio
edificio_santa_isabel.agregar_departamento(departamento1)
edificio_santa_isabel.agregar_departamento(departamento2)
edificio_santa_isabel.agregar_departamento(departamento3)

# Imprimir reporte completo del edificio
print(edificio_santa_isabel)


# Búqeuda simulada

# Buscar por número de departamento
resultado_numero = edificio_santa_isabel.buscar_departamento(402)
print("Búsqueda por número 402:")
for d in resultado_numero:
    print(d)

# Buscar por propietario
resultado_dueno = edificio_santa_isabel.buscar_departamento("Camila Sánchez")
print("\nBúsqueda por propietario 'Camila Sánchez':")
for d in resultado_dueno:
    print(d)

print("Valor UF actual de los departamentos: ")
print(f"Valor UF departamento {departamento1.numero}: ${departamento1.uf}")  # UF: 39700
print(f"Valor UF departamento {departamento2.numero}: ${departamento2.uf}")  # UF: 39700

# Cambiar UF
Departamento.cambiar_valor_uf(40000)

print("Valor UF actual de los departamentos: ")
print(f"Valor UF departamento {departamento1.numero}: ${departamento1.uf}")  # UF: 40000
print(f"Valor UF departamento {departamento2.numero}: ${departamento2.uf}")  # UF: 40000