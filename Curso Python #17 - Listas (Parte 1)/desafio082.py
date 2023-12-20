from random import randint
print("Desáfio 082: Crie um programa que vai ler vários números e colocar em uma lista.")
print("Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados respectivamente.")
print("Ao final, mostre o conteúdo das três listas geradas.")
x = 5

lista = []
lista_pares = []
lista_impares = []

for rodada in range(x):
    valor = randint(1,999999) #int(input(f"Digite o valor da {rodada+1}° rodada: "))

    lista.append(valor)
    print(f"O número: {valor} foi adicionado a lista, veja:", lista)

    if valor % 2 == 0:
        lista_pares.append(valor)
        print(f"O número: {valor} foi adicionado a lista pares, veja:", lista_pares)
    else:
        lista_impares.append(valor)
        print(f"O número: {valor} foi adicionado a lista impares, veja:", lista_impares)

print(50*"=")
print("Veja a lista completa:", lista)
print(50*"=")
print("Veja a lista só de números pares:", lista_pares)
print(50*"=")
print("Veja a lista só de números impares:", lista_impares)
print(50*"=")
