
f = open("Example.txt", "w+")
f.write("Texto de prueba")
f.close()

f2 = open("Example.txt", "r")
datos = f2.read()
f2.close()

print(datos)


