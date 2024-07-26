# Exercício de Casa 🏠 Gerenciando uma Videoteca com SQLite e CSV
#Objetivo: Dominar a integração entre arquivos CSV e bancos de dados SQLite para gerenciar uma videoteca.

#1-Criar um Banco de Dados e a Tabela:
import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()  # Adiciona os parênteses para chamar o método

# Criar a tabela filmes se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        diretor TEXT,
        ano INTEGER,
        genero TEXT,
        preco REAL
    )
''')

# Confirmar a transação
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()

print("Banco de dados videoteca.db e tabela 'filmes' criados com sucesso!")
