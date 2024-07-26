import sqlite3
import csv

conn=sqlite3.connect("videoteca.db")
cursor=conn.cursor()

#Atualiza o preço do filme com id = 2
cursor.execute("DELETE FROM filmes WHERE id = 2")

conn.commit()
cursor.close()
conn.close()