import sqlite3

# Conectar ao banco de dados (ou criar um banco de dados)
conexao = sqlite3.connect('exercicio_join.db')
cursor = conexao.cursor()

# Criar a tabela de clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Criar a tabela de pedidos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY,
        data TEXT NOT NULL,
        valor REAL NOT NULL,
        cliente_id INTEGER,
        FOREIGN KEY (cliente_id) REFERENCES clientes (id)
    )
''')

# Inserir dados na tabela de clientes
clientes = [
    (1, 'Ana', 'ana@example.com'),
    (2, 'Bruno', 'bruno@example.com'),
    (3, 'Carla', 'carla@example.com')
]
cursor.executemany('INSERT INTO clientes VALUES (?, ?, ?)', clientes)

# Inserir dados na tabela de pedidos
pedidos = [
    (1, '2023-07-01', 100.50, 1),
    (2, '2023-07-02', 200.75, 2),
    (3, '2023-07-03', 150.00, 1)
]
cursor.executemany('INSERT INTO pedidos VALUES (?, ?, ?, ?)', pedidos)

# Salvar (commit) as mudanças
conexao.commit()