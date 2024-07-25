import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Seleciona os estudantes com idade maior que 21
cursor.execute("SELECT * FROM estudantes WHERE idade > 21")
registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)

# Fecha a conexão
cursor.close()
conn.close()