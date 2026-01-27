# calculador_inventario.py
class Transaccion:
    def __init__(self, producto: str, cantidad_vendida: int):

        self.producto = producto
        self.cantidad_vendida = cantidad_vendida


class BaseDatosMock:

    def guardar(self, transaccion: Transaccion) -> bool:

       # Simulamos guardar en una base de datos real
        return True


class CalculadoraInventario:
    # Calcula el total de productos en el inventario

    def calcular_total(self, cantidades: list) -> int:

        total = 0
        for cantidad in cantidades:
            total += cantidad
        return total
# Verifica si una cantidad está por debajo del stock mínimo

    def es_bajo_stock(self, cantidad: int, nivel_minimo: int) -> bool:

        return cantidad < nivel_minimo
# Simula guardar una transacción usando una dependencia externa

    def guardar_transaccion(self, transaccion: Transaccion, db_mock:

                            BaseDatosMock) -> bool:

        return db_mock.guardar(transaccion)
