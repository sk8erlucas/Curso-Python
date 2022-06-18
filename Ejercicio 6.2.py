
class Alumno:
    _nombre = ""
    _nota = 0

    def __init__(self, NombreAlumno, NotaAlumno):
        self._nombre = NombreAlumno
        self._nota = NotaAlumno

    def aprobadoDesaprobado(self):
        if self._nota > 4:
            return True
        else:
            return False

NombreAlumnoInput = input("Ingrese el nombre del alumno: ")
NotaAlumnoInput = int(input("Ingrese la nota del del alumno: "))

Alumno1 = Alumno(NombreAlumnoInput, NotaAlumnoInput)

if Alumno1.aprobadoDesaprobado():
    print("\nAlumno aprobado")
else:
    print("\nAlumno desaprobado")

