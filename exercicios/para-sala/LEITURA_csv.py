import csv

with open('produtos.csv', newline='', encoding='utf-8') as csvfile: # Abre o arquivo CSV "produtos.csv" para leitura.(O ARQUIVO TEM QUE TÁ NA PASTA)
    leitor = csv.reader(csvfile) #Cria um leitor CSV para ler as linhas do arquivo.
    for linha in leitor: #ITERA CADA LINHA
        print(linha)