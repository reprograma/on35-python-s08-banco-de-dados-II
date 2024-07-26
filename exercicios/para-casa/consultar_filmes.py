import sqlite3
import csv

conn=sqlite3.connect("videoteca.db")
cursor=conn.cursor()

cursor.execute("SELECT * FROM filmes")
registros = cursor.fetchall()
for registro in registros:
    print(registro)

conn.commit()
cursor.close()
conn.close()
       