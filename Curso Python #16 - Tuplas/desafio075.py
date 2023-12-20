print("Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:")
print(50 * "=")
print("A) Quantas vezes apareceu o valor 9.")
print(50 * "=")
print("B) Em que posição foi o digitado o primeiro valor 3.")
print(50 * "=")
print("C) Quais foram os números pares.")
print(50 * "=")

t = tuple(int(input("Digite um valor: ")) for _ in range(4))
p = sum(1 for valor in t if valor % 2 == 0)

print(f"O número 9 apareceu: {t.count(9)} vezes.")

if 3 in p:
    print(f"O valor 3 está na posição: {t.index(3)}º.")
else:
    print("O valor 3 não foi digitado.")

print(f"O número de valores pares foram: {p}")

