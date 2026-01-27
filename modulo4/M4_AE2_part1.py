class Libros: 
    
    __precio = 0 
    
    def __init__(self, titulo, autor, stock):
        
        self.titulo = titulo
        self.autor = autor
        self.stock = stock
       
    def get_precio(self):
        return
    
    def set_precio(self, precio):
        if precio >=0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo")
            
    def vender(self, unidades):
        if unidades <= 0:
            print("No se puede vender 0 o unidades negativas.")
        elif unidades > self.stock:
            print(f"No hay suficiente stock para vender {unidades} unidades. Stock disponible: {self.stock}")
        else:
            self.stock -= unidades
            print(f"Se vendieron {unidades} unidades de '{self.titulo}'. Stock restante: {self.stock}")
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Stock: {self.stock}")
        print(f"Precio: {self.__precio}")
            
            
libro1 = Libros("1984", "Orwell", 5)
libro1.set_precio(-5000)
libro1.vender(2)
libro1.vender(4)
libro1.mostrar_info()