# Exercício de Casa 🏠 

## Gerenciando uma Videoteca com SQLite e CSV

Neste exercício, você vai se transformar em uma gerente de videoteca e vai usar seus conhecimentos sobre SQLite e CSV para organizar um catálogo de filmes! 

**Objetivo:**  Dominar a integração entre arquivos CSV e bancos de dados SQLite para gerenciar uma videoteca.

**Etapas:**

**1. Crie o Banco de Dados e a Tabela:**

* Crie um banco de dados SQLite chamado `videoteca.db`.
* Crie uma tabela chamada `filmes` com as seguintes colunas:
    * `id` (INTEGER, chave primária, autoincremento)
    * `titulo` (TEXT)
    * `diretor` (TEXT)
    * `ano` (INTEGER)
    * `genero` (TEXT)
    * `preco` (REAL)  

**2. Crie o Arquivo CSV:**

* Crie um arquivo CSV chamado `filmes.csv` com as seguintes colunas:
    * `titulo`
    * `diretor`
    * `ano`
    * `genero`
    * `preco` 
* Adicione pelo menos 5 filmes diferentes ao arquivo `filmes.csv`.

**3. Importe os Dados para o Banco de Dados:**

* Escreva um script Python (chamado `importar_filmes.py`) que leia os dados do `filmes.csv` e os insira na tabela `filmes` no banco de dados `videoteca.db`.

**4. Consulte e Exiba os Dados:**

* Escreva um script Python (chamado `consultar_filmes.py`) que selecione e exiba todos os registros da tabela `filmes`.

**5. Atualize os Dados:**

* Escreva um script Python (chamado `atualizar_filme.py`) que atualize o preço de um filme específico (por exemplo, aumente o preço do filme com `id` 2).

**6. Remova um Filme:**

* Escreva um script Python (chamado `remover_filme.py`) que remova um filme específico da tabela (por exemplo, remova o filme com `id` 3).

**7. Exporte os Dados para um Novo CSV:**

* Escreva um script Python (chamado `exportar_filmes.py`) que exporte os dados da tabela `filmes` para um novo arquivo CSV chamado `exportados_filmes.csv`.

**Exemplo do Arquivo `filmes.csv`:**

```csv
titulo,diretor,ano,genero,preco
O Poderoso Chefão,Francis Ford Coppola,1972,Drama,25.99
O Senhor dos Anéis: A Sociedade do Anel,Peter Jackson,2001,Fantasia,30.99
A Origem,Christopher Nolan,2010,Ficção Científica,19.99
A Vida de Brian,Terry Gilliam,1979,Comédia,15.99
Pulp Fiction,Quentin Tarantino,1994,Crime,22.99
```

**Tarefas Extras (Opcionais):**

* **Validação de Dados:**  Adicione validações para garantir que os dados lidos do CSV sejam válidos antes de serem inseridos no banco de dados. Por exemplo, verifique se o ano é um número válido, se o gênero está dentro de uma lista de gêneros permitidos e se o preço é um número válido.
* **Tratamento de Erros:**  Adicione tratamento de exceções para lidar com possíveis erros durante a leitura, inserção e atualização de dados.
* **Interatividade:** Torne seus scripts interativos, solicitando entradas do usuário para operações como inserção, atualização e remoção de dados.

**Enviando o Exercício:**

Após terminar o exercício, você deve ter os seguintes arquivos:

* `criar_banco.py`
* `importar_filmes.py`
* `consultar_filmes.py`
* `atualizar_filme.py`
* `remover_filme.py`
* `exportar_filmes.py`
* `filmes.csv`

Teste todos os scripts para garantir que eles estejam funcionando corretamente antes de enviar seu trabalho.


**Dicas:**

* Use as ferramentas que aprendeu sobre SQLite e CSV para completar as etapas do exercício.
* Lembre-se de usar o `conn.commit()` para salvar as alterações no banco de dados.
* Feche a conexão com o banco de dados usando `conn.close()`.
* Consulte a documentação do SQLite e do módulo `csv` do Python se precisar de ajuda.

Boa sorte. Vocês vão arrasar! 💜😉



Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [ ] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/mflilian/repo-example/blob/main/exercicios/para-casa/instrucoes-pull-request.md).
