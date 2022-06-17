
def AreaTriangulo(base, altura):
    return (base * altura)/2

def AreaCirculo(radio):
    return (2 * radio)*3.14

baseTrianguloInput = float(input("Ingrese la base del triangulo: "))
alturaTrianguloInput = float(input("Ingrese la altura del triangulo: "))

areaTriangulo = AreaTriangulo(baseTrianguloInput, alturaTrianguloInput)
print("\nEl area es: ", areaTriangulo)

radioCirculoInput = float(input("\nIngrese el radio del circulo: "))
areaCirculo = AreaCirculo(radioCirculoInput)

print("\nEl area es: ", areaCirculo)



