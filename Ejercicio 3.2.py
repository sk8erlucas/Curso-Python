
peso = int(input("Ingrese su peso en kg: "))
estatura = int(input("Ingrese su estatura en metros:"))

indiceMasaCorporal = (peso / estatura) ** 2

print("Tu indice de masa corporal es: ", round(indiceMasaCorporal, 2))