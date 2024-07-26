#**3. Importe os Dados para o Banco de Dados:**

import csv
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Criando a tabela filmes se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        diretor TEXT NOT NULL,
        ano INTEGER,
        genero TEXT NOT NULL,
        preco REAL
)
""")
#Abrindo o arquivo CSV
with open('filmes.csv', newline='', encoding='utf-8') as csvfile:
     leitor = csv.reader(csvfile)
     next(leitor)  # ignora o cabeçalho
     for linha in leitor: #Inserindo cada linha do CSV na tabela
        filme_data = (linha[0], linha[1], int(linha[2]), linha[3], float(linha[4])) #A tupla filme_data é criada agrupando os cinco pontos de dados da linha atual:
        cursor.execute("INSERT INTO filmes(titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)", filme_data)
        #insere a tupla filme_data na tabela filmes
                 
#salvando as mudanças
conn.commit()
#fechando as conexões
cursor.close()
conn.close()