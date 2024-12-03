# 3. Importe os Dados para o Banco de Dados:**

# Escreva um script Python (chamado `importar_filmes.py`) que leia os dados do `filmes.csv` e os insira na tabela `filmes` no banco de dados `videoteca.db`.

import sqlite3
import csv

# Conectar ao banco de dados (ou criar um banco de dados)
conn = sqlite3.connect('banco_dados/videoteca.db')
cursor = conn.cursor()

with open('arquivos_csv/filmes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pula o cabeçalho
    for linha in leitor:
        insert_datas = "INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(insert_datas,(linha[0],linha[1],linha[2],linha[3],linha[4]))

sql_query = ("SELECT * FROM filmes")

cursor.execute(sql_query)
dados = cursor.fetchall() #significa buscar todos os registros que foi selecionada pelo select

# Salva as alterações no banco de dados
conn.commit()

print('Filmes importados para o banco de dados!')

# Fecha a conexão
cursor.close()
conn.close()
