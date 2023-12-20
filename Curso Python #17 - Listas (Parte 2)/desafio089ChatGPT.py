print("Desafio 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.")
print("No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.")

ficha = []

print("-+" * 50)

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar [S/N]? "))
    
    if resp.lower() == 'n':
        break

print("-+" * 50)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')

for i, aluno in enumerate(ficha):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

while True:
    print("-" * 50)
    opc = int(input("Mostrar notas de qual aluno? (Digite 999 para sair) "))
    
    if opc == 999:
        print("Finalizado.")
        break
    
    if 0 <= opc < len(ficha):
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
    else:
        print("Opção inválida. Tente novamente.")
