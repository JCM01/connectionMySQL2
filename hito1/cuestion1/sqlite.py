import sqlite3
import datetime

con = sqlite3.connect('tienda.db')

"""
def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE cliente
    (id integer PRIMARY KEY AUTOINCREMENT, 
    nombre text, 
    apellido text,
     ciudad text,
     fecha text)")
    con.commit()
sql_table(con)
"""

def crud():

    while True:

        print("1. Añadir cliente      ")
        print("2. Listar clientes     ")
        print("3. Modificar cliente   ")
        print("4. Borrar cliente      ")
        print("5. Salir               ")

        option = input("¿Qué quieres hacer?")

        if option == '1':
            print("Se va añadir un cliente\n")
            nombre = input("Dime nombre  ")
            apellidos = input("Dime apellidos ")
            ciudad = input("Dime ciudad ")
            fecha = datetime.datetime.now()
            datos = (nombre, apellidos, ciudad,fecha)

            def sql_insert(con, entities):
                cursorObj = con.cursor()
                cursorObj.execute( 'INSERT INTO cliente(id, nombre, apellido, ciudad, fecha) VALUES(null, ?, ?, ?, ?)' , datos )
                con.commit()
            sql_insert(con, datos)
            print("El cliente se ha añadido\n")

        elif option == '2':
            print("Se está listando los clientes\n")

            def sql_fetch(con):
                cursorObj = con.cursor()
                cursorObj.execute('SELECT * FROM cliente')
                rows = cursorObj.fetchall()
                for row in rows:
                    print(row)
            sql_fetch(con)

        elif option == '3':
           cursorObj = con.cursor()
           id= input("¿Dime la id  que quieras cambiar?  ")
           cursorObj.execute('SELECT * FROM cliente WHERE id='+id+';')
           rows = cursorObj.fetchall()

           for row in rows:
               print(row)

           def update(con):
               cursorObj = con.cursor()
               while True:

                print("[a] Cambiar Nombre")
                print("[b] Cambiar Apellido")
                print("[c] Cambiar Ciudad")
                print("[d] Salir")

                modificar=(input())

                if(modificar=='a'):
                    nombre = input("Dime nombre ")
                    cursorObj.execute('UPDATE cliente SET nombre=?  WHERE id=?;',( nombre,id))
                    con.commit()

                elif(modificar=='b'):
                    apellidos=input("Dime apellidos ")
                    cursorObj.execute('UPDATE cliente SET apellido =? WHERE id=? ;',(apellidos,id))
                    con.commit()

                elif(modificar=='c'):
                    ciudad=input("Dime ciudad")
                    cursorObj.execute('UPDATE cliente SET WHERE ciudad= ? WHERE id=? ;',(ciudad,id))
                    con.commit()

                elif (modificar == 'd'):
                    return False;

           update(con)

        elif option == '4':
            cursorObj = con.cursor()
            cursorObj.execute('SELECT * FROM cliente ;')
            rows = cursorObj.fetchall()
            for row in rows:
                print(row)

            id = input("Dime la id del cliente que quieras borrar ")
            cursorObj.execute('DELETE FROM cliente WHERE id='+id+';')
            con.commit()
            print("Se está borrando cliente\n")
            print("El cliente se ha borrado\n")

        elif option == '5':
            print("Fin\n")
            return False
            break

        input("\nPresiona enter para seguir")

crud()

