# Toda vez que abrirmos um novo arquivo, teremos que dar o comando de import
import sqlite3

# Conectando ao banco de dados (ou criar, se não existir)
conn = sqlite3.connect("escola.db") #data base

# Criando um cursor para executar comandos SQL.
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS estudantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
               )
               """)

#estudantes = [
 #   ('Alice', 21),
 #   ('Bob', 22),
 #   ('Charlie', 23)
#]

# Inserir vários estudantes de uma só vez
#cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?,?)", estudantes)

# Atualiza a idade de Bob para 23
#cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))

# Remove o estudante Charlie
cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))


# Ele salva as mudanças que estão sendo feitas no banco de dados de forma permanente.
# Só esta na minha máquina, quando eu dou esse comando, as alterações para o github
conn.commit()

# Boas práticas e fechamento do cursor (pois podemos trabalhar com mais de um cursor no banco de dados)
cursor.close()

# Esse comando é uma boa prática para não dar problemas.
# Podemos fazer outras solicitações e como fechamos, não irá alterar as alterações feitas no banco
conn.close()

