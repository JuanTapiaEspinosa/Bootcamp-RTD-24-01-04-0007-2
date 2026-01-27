from .departamento import Departamento
from .administracion import Administracion


class Edificio:
    def __init__(self, nombre, direccion, nombre_administrador, telefono_administrador):
        self.__nombre = nombre
        self.__direccion = direccion
        #Agregación
        self.__departamentos = []
        #Composición / Relación fuerte
        self.__administracion = Administracion(nombre_administrador, telefono_administrador)
        
    def agregar_departamento(self, depto):
        
        if isinstance(depto, Departamento):
            self.__departamentos.append(depto)
        else:
            raise TypeError("Solo se puede agregar objetos de tipo Departamento")
    
    
# Búsqueda inteligente

    def buscar_departamento(self, dato):
        resultados = []
        
        for depto in self.__departamentos:
            if isinstance(dato, int) and depto.numero == dato:
                resultados.append(depto)
            elif isinstance(dato, str) and depto.dueño.lower() == dato.lower():
                resultados.append(depto)
                
        return resultados
    
    @property
    def administracion(self):
        return self.__administracion
    
    def __str__(self):
        informacion = f"Edificio: {self.__nombre} | Dirección: {self.__direccion}\n"
        informacion += f"{self.__administracion}\nDepartamentos: \n"
        for depto in self.__departamentos:
            informacion += f"- {depto}\n"
        return informacion