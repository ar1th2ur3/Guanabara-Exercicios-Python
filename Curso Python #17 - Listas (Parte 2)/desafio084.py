
print("Desáfio 084: Faça um programa que leia nome e peso de várias pessoas guardando tudo  em uma lista.")
print("No final, mostre:")
print(" A) Quantas pessoas foram cadastradas.")
print(" B) Uma listagem com as pessoas mais pesadas.")
print(" C) Uma listagem com as pessoas mais leve.")

pessoas_cadastradas = 0
dados = []
pessoasPesadas = []
pessoasLeves = []
pessoas = []



for i in range(5):
    dados.append(str(input("Digite o nome de uma pessoa: ")))
    dados.append(int(input("Digite o peso(kg) de uma pessoa: ")))

    pessoas.append([dados[:]])
    dados.clear()
    pessoas_cadastradas+=1

maiorPeso = max(pessoas)
menorPeso = min(pessoas)

for p in pessoas:
    if p[0][1] >= 50:
        pessoasPesadas.append(pessoas[:])
        for ps in pessoas:
            print(f"O(a) {ps[0][0]}, é bastante pesado(a).")
    else:
        print(f"O(a) {p[0][0]}, é bastante leve!")

print(50*"=")
print(f"O maior peso foi: {maiorPeso} e foi do(a): {pessoasPesadas[0][0]}")
print(f"O menor peso foi: {menorPeso} e foi do(a): {pessoasLeves[0][0]}")






