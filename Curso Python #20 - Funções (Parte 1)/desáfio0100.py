from random import randint

print("Desáfio 0100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().")
print("A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.")

def sorteia():
    numero = []
    for _ in range(5):
        n = randint(0,5)
        numero.append(n)
    print(f"Sorteando 5 valores da lista: {numero} PRONTO!")
    return numero

def somaPar(lista):
    valores_pares = 0
    for i in lista:
        if i % 2 == 0:
            valores_pares += i
    print(f"Somando os valores pares de {lista}, temos: {valores_pares}")
    maior_valor = max(lista)
    return maior_valor
    
numero = sorteia()

somaPar(numero)

