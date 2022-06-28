
ingreso = input("Ingrese paises separados por una coma: ")
paises = set(ingreso.split(sep=','))

print(",".join(sorted(list(set(paises)))))
