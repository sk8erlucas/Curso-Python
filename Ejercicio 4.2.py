
numeroMenor = int(input("Ingrese el numero de inicio: "))
numeroMayor = int(input("Ingrese el numero final: "))

for i in range(numeroMenor, numeroMayor+1):
    if i % 2 != 0: 
        print(i)
