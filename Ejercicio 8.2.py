
class Vehiculo:
    ruedas = 0
    puertas = 0

    def __init__(self, ruedas, puertas):
        self.ruedas = ruedas
        self.puertas = puertas

    def EscribirFichero(self):
        f = open("Vehiculo.txt", "w")
        f.write(f'El vehiculo tiene {self.ruedas} ruedas y {self.puertas} puertas')
        f.close()

auto1 = Vehiculo(4, 2)
auto1.EscribirFichero()

f = open("Vehiculo.txt", "r")
print(f.read())




