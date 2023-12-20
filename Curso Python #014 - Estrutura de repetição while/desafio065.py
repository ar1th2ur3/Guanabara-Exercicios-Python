print("Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.")
print("O programa deve perguntar ao usuário se ele quer continuar a digitar valores.")

lista = []
soma = 0
cont = 0

while True:
    n = int(input("Digite um número: "))
    lista.append(n)

    cont += 1
    soma += n

    continuar = str(input("Você quer continuar? ")).upper()

    if continuar != "S":
        break

if cont == 0:
    print("Nenhum numero foi digitado.")
else:

    media = soma / cont
    maiorValor = max(lista)
    menorValor = min(lista)

    print(f"O menor valor é: {menorValor}")
    print(f"O maior valor é: {maiorValor}")
    print(f"A média entre os números foram: {media}")
    print(f"Foram digitados {cont} números e a soma entre eles é {soma}.")

