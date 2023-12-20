print("Faça um programa que leia um número qualquer e mostre o seu fatorial.")

n = int(input("Digite um número para calcularmos o fatorial: "))
f = 1  # Inicialize a variável f com 1, não com 0
m = 1   # Inicialize a variável m com 1, não com 0

while f <= n:
    m *= f  # Atualize o valor de m multiplicando pelo valor de f
    f += 1

print(f"O fatorial de {n} é: {m}")

"""n = int(input("Digite um número para calcularmos o fatorial: "))

f = 1
m = 1
for i in range(1, n+1):
    m *= f  # Atualize o valor de m multiplicando pelo valor de f
    f += 1
    print(f"O fatorial de {n} é: {m}")
print(f"O fatorial de {n} é: {m}")"""

