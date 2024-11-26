import pandas as pd

dados = {
    "Aluno": ["João", "Maria"],
    "Matemática": [85, 90],
    "Português": [78, 88]
}

df = pd.DataFrame(dados)
df.to_excel("notas.xlsx", index=False)
print("Arquivo notas.xlsx criado com sucesso!")
