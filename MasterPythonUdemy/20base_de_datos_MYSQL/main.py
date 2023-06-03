import mysql.connector
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)
#la conexion ha ido correcta?????
#print(database)

#Cursor que nos permite generar la consulta
cursor = database.cursor()

#crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")


for bd in cursor:
    print(bd)

#"Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10, 2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)


#INSERTAR DATOS EN DATABASE
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'opel', 'astral', 18500)")
#database.commit()

#insertar datos masivos

coches = [
    ('seat', 'ibiza', 5000),
    ('renault', 'clio', 2000),
    ('mercedez', 'CLASS C', 35000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES(null,%s, %s, %s)", coches)

database.commit()

#COMO mostrar todos mis coches:

cursor.execute("SELECT * From vehiculos ")
result = cursor.fetchall()

print("TODOS MIS COCHES!!!!!!!!!!!!!!!!!!")
for coche in result:
    print(coche)

#Como mostrar datos personalizados
 
cursor.execute("SELECT * From vehiculos ")
result = cursor.fetchall()

print("TODAS MIS MARCAS y precios!!!!!!!!!!!!!!!!!!")
for coche in result:
    print(coche[1] , coche[3]) #MARCA y precios

#MOSTRAR SOLO LOS QUE TIENEN UN PRECIO MENOR A 5000

cursor.execute("SELECT * From vehiculos WHERE precio <= 5000 ")
result = cursor.fetchall()

print("TODOS MIS COCHES!!!!!!!!!!!!!!!!!!")
for coche in result:
    print(coche[1], coche[3])

#BORRAR REGISTROS

cursor.execute("DELETE FROM vehiculos WHERE marca = 'opel' ")
database.commit()

"""
puede que al usar tanto la base de datos salga un error, para solucionarlo hay que ir a la parte en donde se
crea el cursor y  pasarle el parametro buffered=True
cursor = database.cursor(buffered=True)

#PARA VER LO QUE HA BORRADO, a continuacion del codigo hay que poner...

print(cursor.rowcount, "borrados!!")
"""

#COMO ACTUALIZAR
cursor.execute("UPDATE vehiculos SET modelo='MERZ' WHERE marca='mercedez'")
database.commit()
print(cursor.rowcount, "Actualizados!!")
