class Docente:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        


class Curso:
    def __init__(self, nombre, docente):
        self.nombre = nombre
        self.docente = docente
        
    def mostrar_info(self):
        print(f"Curso: {self.nombre}")
        print(f"Docente: {self.docente.nombre}")
        print(f"Especialidad: {self.docente.especialidad}")

class Alumno:
    def __init__(self, nombre, edad, cursos):
        self.nombre = nombre
        self.edad = edad
        self.cursos = cursos
        
    def mostrar_cursos(self):
        print(f"Cursos de {self.nombre}:")
        for curso in self.cursos:
            curso.mostrar_info()
            print("-" * 20)
            
            
            
# Crear docentes
d1 = Docente("Ana", "Matemática")
d2 = Docente("Luis", "Historia")

# Crear cursos
c1 = Curso("Álgebra", d1)
c2 = Curso("Historia Moderna", d2)

# Crear alumno
alumno = Alumno("Juan", 20, [c1, c2])

# Mostrar cursos del alumno
alumno.mostrar_cursos()