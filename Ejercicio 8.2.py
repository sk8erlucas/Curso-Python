import pickle

class Vehiculo:
    ruedas = 0
    puertas = 0

    def __init__(self, ruedas, puertas):
        self.ruedas = ruedas
        self.puertas = puertas

    def getRuedas(self):
        return self.ruedas

    def __str__(self):
        return (f'El vehiculo tiene {self.ruedas} ruedas y {self.puertas} puertas')

auto1 = Vehiculo(4, 2)

f = open("Vehiculo.bin", "wb")

pickle.dump(auto1, f)
f.close()

f2 = open("Vehiculo.bin", "rb")
auto2 = pickle.load(f2)
f2.close

print(auto2)




