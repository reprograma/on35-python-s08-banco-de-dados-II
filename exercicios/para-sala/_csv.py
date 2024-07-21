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

# Consulta 1: Obter todos os pedidos com os dados dos clientes
cursor.execute('''
    SELECT pedidos.id, pedidos.data, pedidos.valor, clientes.nome, clientes.email
    FROM pedidos
    JOIN clientes ON pedidos.cliente_id = clientes.id
''')
resultado = cursor.fetchall()
print("Pedidos com dados dos clientes:")
for linha in resultado:
    print(linha)

# Consulta 2: Obter todos os clientes que não têm pedidos
cursor.execute('''
    SELECT clientes.id, clientes.nome, clientes.email
    FROM clientes
    LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
    WHERE pedidos.id IS NULL
''')
resultado = cursor.fetchall()
print("\nClientes sem pedidos:")
for linha in resultado:
    print(linha)

# Fechar o cursor
cursor.close()
# Fechar a conexão
conexao.close()