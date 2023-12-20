print("Desáfio 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionario.")
print("No final, mostre o conteúdo da estrutura na tela.")

aluno = {}

aluno['nome'] = str(input("Qual é o nome do Aluno? "))

aluno['média'] = float(input(f"Qual é a média do(a) {aluno['nome']} ?"))

if aluno['média'] < 5:
    aluno['situação'] = 'reprovado'

print(f"O(a) {aluno['nome']} com a média {aluno['média']} está: {aluno['situação']}")