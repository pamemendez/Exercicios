
import csv
with open('alunos.csv', mode='r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
