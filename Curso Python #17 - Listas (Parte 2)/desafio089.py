print("Desáfio 089: Crie um programa que leia nome e duas notas de vários alunos e guarda tudo em uma lista composta.")
print("No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.")


ficha = []

print("-+" * 50)
while True:
    nome = str(input("Nome"))
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar [S/N] ? "))
    if resp in "Nn":
        break

print("-+" * 50)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    print("-" * 50)
    opc = int(input("Mostrar notas de qual aluno ? "))
    if opc == 999:
        print("Finalizado.")
        break
    if opc <= len(ficha) -1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")