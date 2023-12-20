from random import randint

print("Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.")
print(50 * "=")
print("Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.")
print(50 * "=")

# Gere cinco números aleatórios e coloque em uma tupla
numeros_aleatorios = tuple(randint(1, 20) for _ in range(5))

# Mostre a listagem de números gerados
print("Números gerados:", numeros_aleatorios)

# Indique o menor e o maior valor na tupla
menor_valor = min(numeros_aleatorios)
maior_valor = max(numeros_aleatorios)

print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
