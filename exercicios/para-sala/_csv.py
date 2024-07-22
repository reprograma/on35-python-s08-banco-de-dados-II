import sqlite3

# Conectar ao banco de dados (ou criar um banco de dados)
conexao = sqlite3.connect('banco_dados/exercicio_join.db')
cursor = conexao.cursor()

# Criar a tabela de clientes
create_table = ('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

cursor.execute(create_table)

# Criar a tabela de pedidos
create_table = ('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY,
        data TEXT NOT NULL,
        valor REAL NOT NULL,
        cliente_id INTEGER,
        FOREIGN KEY (cliente_id) REFERENCES clientes (id)
    )
''')

cursor.execute(create_table)

# Inserir dados na tabela de clientes
clientes = [
    (1, 'Ana', 'ana@example.com'),
    (2, 'Bruno', 'bruno@example.com'),
    (3, 'Carla', 'carla@example.com')
]
insert_datas = ('INSERT INTO clientes VALUES (?, ?, ?)')

cursor.executemany(insert_datas, clientes)

# Inserir dados na tabela de pedidos
pedidos = [
    (1, '2023-07-01', 100.50, 1),
    (2, '2023-07-02', 200.75, 2),
    (3, '2023-07-03', 150.00, 1)
]
insert_datas = ('INSERT INTO pedidos VALUES (?, ?, ?, ?)')

cursor.executemany(insert_datas, pedidos)

# Salvar (commit) as mudanças
conexao.commit()

# Consulta 1: Obter todos os pedidos com os dados dos clientes
sql_query = ('''
    SELECT pedidos.id, pedidos.data, pedidos.valor, clientes.nome, clientes.email
    FROM pedidos
    JOIN clientes ON pedidos.cliente_id = clientes.id
''')

cursor.execute(sql_query)
resultado = cursor.fetchall()
print("Pedidos com dados dos clientes:")
for linha in resultado:
    print(linha)

# Consulta 2: Obter todos os clientes que não têm pedidos
sql_query = ('''
    SELECT clientes.id, clientes.nome, clientes.email
    FROM clientes
    LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
    WHERE pedidos.id IS NULL
''')
cursor.execute(sql_query)
resultado = cursor.fetchall()
print("\nClientes sem pedidos:")
for linha in resultado:
    print(linha)

# Fechar o cursor
cursor.close()
# Fechar a conexão
conexao.close()