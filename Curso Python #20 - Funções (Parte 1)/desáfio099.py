from random import randint
print("Desáfio 99: Faça um programa que tenha uma funçaõ chamada maior(), que receba vários parâmetros com valores inteiros.")
print("Seu programa tem que analisar todos os valores e dizer qual deles é o maior.")

l = []

def maior(*valores):
    l.extend(valores)
    """print(f"{l}")"""
    return l

c = randint(0, 100)

for _ in range(c):
    valor = randint(0, 9999)
    maior(valor)

print(l)
maior_valor = max(l)

print(50 * "-=")
print("O maior valor é:", maior_valor)