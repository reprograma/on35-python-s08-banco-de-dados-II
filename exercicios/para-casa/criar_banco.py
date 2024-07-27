# **1. Crie o Banco de Dados e a Tabela:**

# * Crie um banco de dados SQLite chamado `videoteca.db`.
# * Crie uma tabela chamada `filmes` com as seguintes colunas:
#     * `id` (INTEGER, chave primária, autoincremento)
#     * `titulo` (TEXT)
#     * `diretor` (TEXT)
#     * `ano` (INTEGER)
#     * `genero` (TEXT)
#     * `preco` (REAL)  

# **2. Crie o Arquivo CSV:**

# * Crie um arquivo CSV chamado `filmes.csv` com as seguintes colunas:
#     * `titulo`
#     * `diretor`
#     * `ano`
#     * `genero`
#     * `preco` 
# * Adicione pelo menos 5 filmes diferentes ao arquivo `filmes.csv`.

# **3. Importe os Dados para o Banco de Dados:**

# * Escreva um script Python (chamado `importar_filmes.py`) que leia os dados do `filmes.csv` e os insira na tabela `filmes` no banco de dados `videoteca.db`.

# **Exemplo do Arquivo `filmes.csv`:**

# ```csv
# titulo,diretor,ano,genero,preco
# O Poderoso Chefão,Francis Ford Coppola,1972,Drama,25.99
# O Senhor dos Anéis: A Sociedade do Anel,Peter Jackson,2001,Fantasia,30.99
# A Origem,Christopher Nolan,2010,Ficção Científica,19.99
# A Vida de Brian,Terry Gilliam,1979,Comédia,15.99
# Pulp Fiction,Quentin Tarantino,1994,Crime,22.99
# ```

import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Cria a tabela filmes
cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    diretor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    genero TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

conn.commit()

# Fecha a conexão
cursor.close()
conn.close()