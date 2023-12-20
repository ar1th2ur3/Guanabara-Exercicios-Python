def separator():
    print("*" * 50)

separator()
n1 = int(input("Digite a primeira nota do aluno:"))

separator()
n2 = int(input("Digite a segunda nota do aluno:"))

media = (n1 + n2) / 2

separator()
print(f"A média de {n1} e {n2} é: {media:.1f}")

separator()
