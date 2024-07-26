import sqlite3
import csv

conn=sqlite3.connect("videoteca.db")
cursor=conn.cursor()

#Atualiza o preço do filme com id = 3
cursor.execute("UPDATE filmes SET preco = ? WHERE id = ?", (28.99, 3))

conn.commit()
cursor.close()
conn.close()