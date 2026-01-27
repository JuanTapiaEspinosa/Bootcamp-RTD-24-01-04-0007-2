class Administracion:
    def __init__(self, nombre_administrador, telefono_administrador):
        self.__nombre_administrador = nombre_administrador
        self.__telefono_administrador = telefono_administrador
    
    @property
    def nombre_administrador(self):
        return self.__nombre_administrador
    
    @property
    def telefono_administrador(self):
        return self.__telefono_administrador
    
    def __str__(self):
        return f"Administrador: {self.__nombre_administrador} | Teléfono: {self.__telefono_administrador}"