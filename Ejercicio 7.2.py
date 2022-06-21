import time

horaActual = time.localtime()[3]

print("Son las ", horaActual, " horas")

if (horaActual > 7):
    print("Hora de ir a casa")
else:
    print("Faltan ", 7-horaActual, " horas para ir a casa")
