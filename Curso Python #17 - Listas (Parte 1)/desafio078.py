print("Desafio 078: Faça um programa que leia 5 valores númericos e guarde-os em uma lista. ")
print(50 * "=")
print("No final, mostre qual foi o maior e o menor vlaor digitado e as suas respectivas posições na lista.")
print(50 * "=")

maiorValor = 0
menorValor = 0
l = []
c = 5

for i in range(c):
    l.append(int(input("Digite um valor:")))


mv = max(l)
mn = min(l)


print(50 * "=")
print(f"Os valores são: {l}")

for i, v in enumerate(l):
    print(f"O valor {v} está na posição: {i+1}")
    
    if v == mv:
        maiorValor = mv
    if v == mn:
        menorValor = mn

print(50 * "=")
print(f"O maior valor é: {maiorValor} e está na posição: {l.index(maiorValor)}")
print(f"O menor valor é: {menorValor} e está na posição: {l.index((menorValor))}")
print(50 * "=")
    


