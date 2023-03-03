import sqlite3
import os.path
import getpass
def main():
    agregrarAlumno(9,"pedro","pedrero")
    agregrarAlumno(10,"edgar","ruiz")
    agregrarAlumno(11,"jorge","estrada")
    agregrarAlumno(12,"pineda","pandd")
    agregrarAlumno(13,"ndd","djdjdj")
    agregrarAlumno(14,"djdikdj","dkdjdj")
    agregrarAlumno(15,"djdjd","dkdkd")
    agregrarAlumno(16,"eddmdmd","ddddd")
    buscarAlumno("pedro")
def agregrarAlumno(id,nombre,apellido):
     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
     db_path = os.path.join(BASE_DIR, "alumnos2.db")
     with sqlite3.connect(db_path) as db:
      cursor=db.cursor()
      query='''INSERT INTO data(id,name,apellido) VALUES(?,?,?)'''
      rows=cursor.execute(query, (id,nombre,apellido) )
      print(type(rows))


def buscarAlumno(nombre):
     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
     db_path = os.path.join(BASE_DIR, "alumnos2.db")
     with sqlite3.connect(db_path) as db:
      cursor=db.cursor()
      query=f"SELECT * FROM data WHERE name='{nombre}'"
      rows=cursor.execute(query )
     for row in rows:
        print(row)
           
main()