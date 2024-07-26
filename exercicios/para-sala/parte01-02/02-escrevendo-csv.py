# Escrita em CSV:

import csv
funcionarios = [
    [1,'Milena','TI'],
    [2, 'Ellen', 'Desenvolvimento'],
    [3, 'Danda', 'Dados'],
    [4, 'Camila', 'Prof']
]
with open('funcionarios.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id', 'nome', 'departamento'])
    escritor.writerows(funcionarios)