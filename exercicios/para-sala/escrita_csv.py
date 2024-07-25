import csv

funcionarios = [
    [1, 'Ana', 'Financeiro'],
    [2, 'Carlos', 'TI'],
    [3, 'Beatriz', 'RH']
]

with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'departamento'])  # Escreve o cabeçalho
    escritor.writerows(funcionarios)  # Escreve os dados