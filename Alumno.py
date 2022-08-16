class Alumno:

    def __init__(self, nombre,legajo):
        self.nombre = nombre
        self.legajo = legajo
    
    def __str__(self):
        return f"El alumno {self.nombre}, tiene el legajo {self.legajo}"