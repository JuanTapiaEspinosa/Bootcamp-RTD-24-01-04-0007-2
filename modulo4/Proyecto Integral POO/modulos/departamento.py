class Departamento:
    def __init__(self, numero, dueño, metros2, saldo_gastos_comunes):
        self.__numero = numero
        self.__dueño = dueño
        self.__metros2 = metros2
        self.__saldo_gastos_comunes = saldo_gastos_comunes

    @property
    def numero(self):
        return self.__numero
    
    @property
    def dueño(self):
        return self.__dueño
    

    @property
    def saldo_gastos_comunes(self):
        return self.__saldo_gastos_comunes

    def pagar_gastos(self, monto):

        if monto <= 0:
            raise ValueError("El monto a pagar debe ser positivo")
        if monto > self.__saldo_gastos_comunes:
            raise ValueError("El monto no puede superar la deuda")

        self.saldo_gastos_comunes -= monto

    def __str__(self):
        return f"Unidad: {self.__numero} | Propietario: {self.__dueño} | Metros cuadrados: {self.__metros2} | Deuda total: ${self.__saldo_gastos_comunes}"
