<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Aprofundando em banco de dados relacional SQL

## Turma ON35 | Python | Semana 8 | 2024 | Professora Camila Ribeiro

## Instruções

1. **Faça o Fork deste repositório!** 
    - Clique no botão "Fork" no canto superior direito da página do repositório.
    - Você terá uma cópia do repositório em sua conta do GitHub.
2. **Clone o repositório na sua máquina:**
    - Abra o seu terminal e digite:
    ```bash
    git clone https://github.com/seu-usuario/on35-python-s08-banco-de-dados-II.git
    ```
    - Substitua "seu-usuario" pelo seu nome de usuário do GitHub.
3. **Entre na pasta do repositório:**
    - Abra o seu terminal e digite:
    ```bash
    cd on35-python-s08-banco-de-dados-II.git
    ```
## Introdução

Você já se perguntou como os dados são organizados em aplicativos e sites?  Imagine um sistema de organização poderoso e fácil de usar que você pode levar para qualquer lugar!  Essa é a magia do SQLite, um sistema de gerenciamento de banco de dados (SGBD) leve, autocontido e embutido, perfeito para suas ideias e projetos.

Nesta aula, vamos explorar o mundo do SQLite e aprender como integrá-lo com arquivos CSV, um formato de dados popular e simples. Você aprenderá a:

**Objetivos:**

* **Entender os fundamentos do SQLite:** Descubra como o SQLite funciona e suas vantagens para iniciantes e projetos menores.
* **Criar seu próprio banco de dados SQLite:** Aprenda a usar Python para criar e conectar-se a um banco de dados SQLite.
* **Dominar a linguagem SQL:**  Domine os comandos básicos do SQL (SELECT, INSERT, UPDATE, DELETE) para manipular dados no SQLite.
* **Conectar tabelas com JOIN e LEFT JOIN:**  Aprenda a combinar informações de diferentes tabelas para obter insights poderosos.
* **Importar dados de arquivos CSV:** Descubra como importar dados de arquivos CSV para o SQLite, organizando suas informações de forma eficiente.
* **Exportar dados para arquivos CSV:**  Aprenda a exportar dados do SQLite para arquivos CSV, facilitando o compartilhamento e análise de seus dados.

## Introdução ao SQLite

SQLite é um sistema de gerenciamento de banco de dados relacional (SGBD) leve, autocontido e embutido. Ele é amplamente utilizado em aplicativos que requerem um banco de dados eficiente, sem a necessidade de um servidor separado.

**Por que o SQLite é tão especial?**

* **Simplicidade:**  Ele não precisa de um servidor externo para funcionar, o que o torna ideal para iniciantes e projetos pequenos.
* **Flexibilidade:**  Pode ser usado em diversos sistemas operacionais (Windows, macOS, Linux) e até mesmo em dispositivos móveis.
* **Eficiência:**  O SQLite é rápido e confiável, garantindo que seus dados estejam sempre seguros e acessíveis.

**O SQLite é perfeito para:**

* **Gerenciar suas finanças:**  Crie um banco de dados para acompanhar suas despesas, receitas e investimentos.
* **Organizar suas coleções:**  Crie listas detalhadas de seus livros, filmes, músicas ou qualquer outra coleção que você ama.
* **Criar aplicativos simples:**  Use o SQLite para armazenar dados em seus programas, como jogos, aplicativos de tarefas e muito mais.

**Começando com o SQLite**

Para usar o SQLite, você precisará de uma linguagem de programação, como Python.  O Python é uma linguagem amigável e popular, perfeita para iniciantes.

1. **Instalando o Python:** Acesse o site oficial do Python (https://www.python.org/) e baixe a versão mais recente para o seu sistema operacional. Siga as instruções de instalação para configurar o Python em seu computador.

2. **Importando o módulo `sqlite3`:** O Python já inclui o módulo `sqlite3` para interagir com bancos de dados SQLite.  Para usá-lo, basta importar o módulo em seu script Python:

   ```python
   import sqlite3
   ```

**Criando seu Primeiro Banco de Dados SQLite**

É hora de colocar a mão na massa e criar seu primeiro banco de dados!  Usaremos o Python para isso.  

1. **Crie um novo arquivo Python:** Abra um editor de código e salve um novo arquivo com a extensão `.py` (por exemplo, `meu_banco_de_dados.py`).

2. **Conecte-se ao seu banco de dados:**  A função `sqlite3.connect()`  é como uma chave mágica que abre as portas para o seu banco de dados.  Se o banco de dados não existir, ele será criado automaticamente.

   ```python
   import sqlite3

   # Conectando ao banco de dados (ou criando, se não existir)
   conn = sqlite3.connect('meu_banco_de_dados.db') 

   # Criando um cursor para executar comandos SQL
   cursor = conn.cursor()
   ```

*   **`conn = sqlite3.connect('meu_banco_de_dados.db')`:**  Essa linha conecta seu script Python a um arquivo chamado `meu_banco_de_dados.db`. Se esse arquivo não existir, ele será criado automaticamente. 
*   **`cursor = conn.cursor()`:**  Essa linha cria um "cursor", que é como um ponteiro que você usa para interagir com o banco de dados.  Com o cursor, você pode executar comandos SQL para adicionar, editar, excluir e consultar dados.

**Comandos Mágicos: Linguagem SQL**

Para falar com o SQLite, você precisa de uma linguagem especial chamada SQL (Structured Query Language).  Ela é bem intuitiva, como um idioma simplificado para organizar dados.  Vamos aprender alguns comandos básicos:

1. **`SELECT`:**  Buscar informações no banco de dados, como se você estivesse procurando uma receita no seu livro de culinária.

   ```python
   
   # Selecionando todos os registros de uma tabela
   cursor.execute("SELECT * FROM filmes")

   # Recuperando todos os resultados da consulta
   filmes = cursor.fetchall()

   # Exibindo os resultados
    print("Lista de Filmes na Videoteca:") 
    print("-" * 50)  # separa cada item por pontinhado
    for filme in filmes:
        print(f"ID: {filme[0]}")
        print(f"Título: {filme[1]}")
        print(f"Diretor: {filme[2]}")
        print(f"Ano: {filme[3]}")
        print(f"Gênero: {filme[4]}")
        print(f"Preço: R$ {filme[5]:.2f}")
        print("-" * 50) # separa cada item por pontinhado
   ```

2. **`INSERT`:** Adicionar novas informações ao banco de dados, como se você estivesse escrevendo um novo capítulo no seu diário.

   ```python
   # Inserindo um novo registro na tabela
   cursor.execute("""
     INSERT INTO minha_tabela(coluna1, coluna2)
     VALUES (?, ?)
    """, (valor1, valor2))

   # Salvando (commit) as mudanças
   conn.commit()
   ```

3. **`UPDATE`:**  Atualizar informações, como se você estivesse corrigindo um erro em um documento.

   ```python

    # Atualizando o preço do filme com id 2
    novo_preco = 19.99  # Novo preço para o filme
    id_filme = 2  # ID do filme que queremos atualizar
   
   # Atualizando um registro existente
   cursor.execute("""
       UPDATE minha_tabela
       SET coluna1 = ?
       WHERE coluna2 = ?"
   """, (novo_preco, id_filme))  

   # Salvando as mudanças
   conn.commit()
   ```

4. **`DELETE`:**  Remover informações, como se você estivesse apagando um rascunho de um texto.

   ```python

    # ID do filme que queremos remover
    id_filme = 3
   
   # Removendo um registro da tabela
   cursor.execute("""
     DELETE FROM minha_tabela
     WHERE coluna1 = ?"
   """, (id_filme,))  

   # Salvando as mudanças
   conn.commit()
   ```

**Conectando Tabelas com JOIN e LEFT JOIN**

Imagine que você tem duas tabelas, uma com dados sobre clientes e outra com dados sobre pedidos.  O comando `JOIN`  é como uma ponte que conecta essas tabelas, permitindo que você encontre informações sobre quais clientes fizeram quais pedidos.

1. **`JOIN`:** Combina registros de duas ou mais tabelas com base em uma coluna relacionada.

   ```python
   # Selecionando dados de duas tabelas relacionadas
   cursor.execute("""
   SELECT a.coluna1, b.coluna2
   FROM tabela1 a
   JOIN tabela2 b ON a.chave_estrangeira = b.id
   """)
   resultados = cursor.fetchall()

   for linha in resultados:
       print(linha)
   ```

2. **`LEFT JOIN`:** Retorna todos os registros da tabela à esquerda e os correspondentes da tabela à direita, incluindo NULL caso não haja correspondência.

   ```python
   # Selecionando dados com LEFT JOIN
   cursor.execute("""
   SELECT a.coluna1, b.coluna2
   FROM tabela1 a
   LEFT JOIN tabela2 b ON a.chave_estrangeira = b.id
   """)
   resultados = cursor.fetchall()

   for linha in resultados:
       print(linha)
   ```

**Fechando a Conexão**

Após executar todos os comandos necessários, é importante fechar a conexão com o banco de dados para liberar os recursos.

   ```python
   # Fechando o cursor e a conexão
   cursor.close()
   conn.close()
   ```

**Exemplo Completo: Criando, Inserindo, Atualizando, Selecionando, Deletando e Usando JOIN**

```python
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Criando uma tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Inserindo dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Bob", 25))

# Atualizando dados
cursor.execute("UPDATE usuarios SET idade = ? WHERE nome = ?", (26, "Bob"))

# Selecionando dados
cursor.execute("SELECT * FROM usuarios")
for linha in cursor.fetchall():
    print(linha)

# Removendo dados
cursor.execute("DELETE FROM usuarios WHERE nome = ?", ("Alice",))

# Commit das mudanças
conn.commit()

# Fechando a conexão
cursor.close()
conn.close()
```

**Explorando o SQLite com Visual Studio Code**

O Visual Studio Code (VS Code) é um editor de código gratuito e poderoso, que pode ser usado para trabalhar com o SQLite de forma mais eficiente.  Para facilitar sua jornada, você pode instalar algumas extensões que irão tornar o processo de desenvolvimento mais simples e intuitivo:

* **SQLite:** Essa extensão essencial oferece recursos para abrir e editar arquivos SQLite (.db), executar consultas SQL, visualizar dados e até mesmo criar tabelas e colunas diretamente no VS Code.


* **SQLite Viewer:**  Com o SQLite Viewer, você pode visualizar seus dados SQLite de forma gráfica, sem precisar escrever código. Ele oferece uma interface simples e amigável para navegar pelas tabelas, visualizar os dados e editar registros.


**Integração com CSV: Organizando Dados de forma Simples**

O SQLite pode ser usado para importar dados de um arquivo CSV (Comma Separated Values) para o SQLite, como se estivesse organizando um álbum de fotos em um fichário.  Também é possível exportar dados do SQLite para um CSV,  como se você estivesse imprimindo fotos para compartilhar com amigos.

**Bibliotecas Necessárias**

Para este tutorial, vamos usar as bibliotecas `sqlite3` e `csv`, ambas inclusas na biblioteca padrão do Python. Certifique-se de que você tenha o Python instalado.

**Instalando e Importando as Bibliotecas**

Como `sqlite3` e `csv` são bibliotecas padrão do Python, não é necessário instalar pacotes adicionais. Para usá-las, basta importá-las no seu script Python:

```python
import sqlite3
import csv
```

**Lendo Dados de um Arquivo CSV e Inserindo no SQLite**

Vamos começar lendo dados de um arquivo CSV e inserindo-os em uma tabela do banco de dados SQLite.

1. **Criando a Tabela no SQLite**

Primeiro, vamos criar uma tabela no banco de dados SQLite onde os dados do CSV serão armazenados. Suponha que temos um arquivo CSV chamado `dados.csv` com as colunas `nome` e `idade`.

```python
import sqlite3

# Conectando ao banco de dados SQLite (ou criando se não existir)
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Criando a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Salvando as mudanças
conn.commit()
```

2. **Lendo o Arquivo CSV e Inserindo Dados na Tabela**

Agora, vamos ler o arquivo CSV e inserir os dados na tabela `usuarios`.

```python
import csv
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Abrindo o arquivo CSV
with open('dados.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Pulando o cabeçalho
    next(leitor_csv)
    
    # Inserindo cada linha do CSV na tabela
    for linha in leitor_csv:
        cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (linha[0], int(linha[1])))

# Salvando as mudanças
conn.commit()

# Fechando a conexão
cursor.close()
conn.close()
```

**Exportando Dados do SQLite para um Arquivo CSV**

Vamos exportar dados da tabela `usuarios` para um arquivo CSV.

```python
import csv
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# Selecionando todos os dados da tabela
cursor.execute("SELECT nome, idade FROM usuarios")
dados = cursor.fetchall()

# Escrevendo os dados para um arquivo CSV
with open('exportados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escrevendo o cabeçalho
    escritor_csv.writerow(['nome', 'idade'])
    
    # Escrevendo os dados
    escritor_csv.writerows(dados)

# Fechando a conexão
cursor.close()
conn.close()
```

**Exemplo Completo**

Aqui está um exemplo completo que demonstra como ler dados de um arquivo CSV e inseri-los no SQLite, e como exportar dados do SQLite para um arquivo CSV.

```python
import sqlite3
import csv

# Função para criar a tabela no SQLite
def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    """)
    conn.commit()

# Função para inserir dados do CSV no SQLite
def importar_csv_para_sqlite(arquivo_csv, conn):
    cursor = conn.cursor()
    with open(arquivo_csv, 'r') as csv_file:
        leitor_csv = csv.reader(csv_file)
        next(leitor_csv)  # Pular o cabeçalho
        for linha in leitor_csv:
            cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (linha[0], int(linha[1])))
    conn.commit()

# Função para exportar dados do SQLite para CSV
def exportar_sqlite_para_csv(arquivo_csv, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT nome, idade FROM usuarios")
    dados = cursor.fetchall()
    with open(arquivo_csv, 'w', newline='') as csv_file:
        escritor_csv = csv.writer(csv_file)
        escritor_csv.writerow(['nome', 'idade'])  # Cabeçalho
        escritor_csv.writerows(dados)

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('exemplo.db')

# Criando a tabela
criar_tabela(conn)

# Importando dados do CSV para o SQLite
importar_csv_para_sqlite('dados.csv', conn)

# Exportando dados do SQLite para CSV
exportar_sqlite_para_csv('exportados.csv', conn)

# Fechando a conexão
conn.close()
```

<br>


## 🔗Links Úteis

* **[Link para um tutorial de SQLite](https://www.tutorialspoint.com/sqlite/sqlite_tutorial.htm):**  Aprofunde seu conhecimento com este tutorial interativo.
* **[Link para um fórum de dúvidas sobre SQLite](https://www.sqlite.org/forum/forum.html):**  Se você tiver alguma dúvida, encontre respostas nesse fórum online.

<br>

---

<br>

<p align="center">
Desenvolvido com :purple_heart:  
</p>
