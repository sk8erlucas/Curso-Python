
def anioBisiesto(anio):

    if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        return True
    else:
        return False

y: int = int(input("Ingrese un ano: "))

if anioBisiesto(y) == True:
    print(f"El anio {y} es bisiesto")
else:
    print(f"El anio {y} no es bisiesto")