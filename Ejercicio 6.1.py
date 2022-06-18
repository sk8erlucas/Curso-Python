
class Vehiculo:
    _color = ""
    _ruedas = 0
    _puertas = 0

class Coche(Vehiculo):
    _velocidad = 0
    _Cilindrada = 0

    def __init__(self, color, puertas, velocidad, cilindrada):
        self._ruedas = 4
        self._color = color
        self._puertas = puertas
        self._velocidad = velocidad
        self._Cilindrada = cilindrada

    def MostrarValores(self):
        print("El coche tiene", self._ruedas, "ruedas")
        print("El coche es de color", self._color)
        print("El coche tiene", self._puertas, "puertas")
        print("El coche va a", self._velocidad)
        print("El coche tiene una cilindrada de", self._Cilindrada)


NuevoCoche = Coche("Rojo", 4, 0, 1600)
NuevoCoche.MostrarValores()
