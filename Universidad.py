class Universidad:

    def __init__(self):
        self.alumnos = []
    
    def agregarAlumno(self, alumno):
        self.alumno.append(alumno)
    
    def listarAlumnos(self):
        for alumno in self.alumnos:
            print(alumno)
    
    def eliminarAlumno(self, legajo):
        for alumno in self.alumnos:
            if alumno.getLegajo() == legajo:
                self.alumnos.remove(alumno)