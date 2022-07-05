import sqlite3

con = sqlite3.connect('alumnos.db')
cursor = con.cursor()

def crearAlumno(nombre, apellido):
    query = f"INSERT INTO alumnos (nombre, apellido) VALUES('{nombre}', '{apellido}')"
    result = cursor.execute(query)
    con.commit()

crearAlumno("Prueba1", "Prueba")
crearAlumno("Prueba2", "Prueba")
crearAlumno("Prueba3", "Prueba")
crearAlumno("Prueba4", "Prueba")
crearAlumno("Prueba5", "Prueba")
crearAlumno("Prueba6", "Prueba")
crearAlumno("Prueba7", "Prueba")
crearAlumno("Prueba8", "Prueba")

rows = cursor.execute('SELECT * FROM alumnos')

for row in rows:
    print (row)

busqueda = input("\nIngresa el nombre a buscar:")

query = f"SELECT id FROM alumnos WHERE nombre='{busqueda}'"

result = cursor.execute(query).fetchone()

print(result)

cursor.close()
con.close()