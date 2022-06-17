
def esPrimo(numero):
    if numero == 0 or numero == 1:
        return False
    else:
        for i in range(2, numero):
            if (numero % i == 0):
               return False;

        return True

InputNumero = int(input("Ingrese un numero: "))

resultado = esPrimo(InputNumero)

if resultado == False:
    print(InputNumero, " no es primo")
else:
    print(InputNumero, " si es primo")
