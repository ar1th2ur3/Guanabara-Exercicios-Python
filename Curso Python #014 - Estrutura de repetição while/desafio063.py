print("Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos da sequência de Fibonacci.")

n = int(input("Digite um número inteiro qualquer: "))

# Inicializa as variáveis para os primeiros dois termos da sequência
a, b = 0, 1

cont = 0  # Inicializa um contador para controlar o número de termos mostrados

while cont < n:
    print(a, end=" ")  # Imprime o termo atual
    a, b = b, a + b  # Calcula o próximo termo da sequência
    cont += 1  # Incrementa o contador

print()  # Pula para a próxima linha após mostrar todos os termos
