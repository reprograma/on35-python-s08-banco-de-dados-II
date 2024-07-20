import csv

with open('produtos.csv', newline='', encoding='UTF-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print(linha)