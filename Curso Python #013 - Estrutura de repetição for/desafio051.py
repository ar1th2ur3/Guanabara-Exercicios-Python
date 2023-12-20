print("Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.")

primeiro = int(input("Primeiro elemento: "))
razao = int(input("Razão: "))
n = 10

ultimo = primeiro + (n - 1) * razao  # Calcula o décimo termo da progressão
# O loop irá de 'primeiro' até 'ultimo', incrementando em 'razao'
for termo in range(primeiro, ultimo + razao, razao):
    print(termo)
