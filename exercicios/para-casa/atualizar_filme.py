import sqlite3

#Conect to data base
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

#Set new price to movie id = 2
cursor.execute('''
               UPDATE filmes
               SET preco = 29
               WHERE id = 2
               ''')

#Save changes
conn.commit()
conn.close()

