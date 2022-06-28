from functools import reduce

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]

def verImpares(x):
    if x % 2 == 0:
        return False
    else:
        return True

result = filter(verImpares, listaNumeros)
print(list(result))

def sumar(a, b):
    return a + b

suma = reduce(sumar, listaNumeros)
print(suma)
