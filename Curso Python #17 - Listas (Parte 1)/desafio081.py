print("Desáfio 081: Crie um programa que vai ler vários números e colocar em uma lista.")
print("Depois disso, mostre:")

print("A) Quantos números foram digitados:")
print("B) A lista de valores ordenada de forma decrescente.")
print("C) Se o valor 5 foi digitado e está ou não na lista.")

def separador():
    print(50 * "=")

lista = []
for _ in range(1,6):
    numero = int(input(f"{_}* valor desejado. Digite: "))
    lista.append(numero)
    print(f"O número: {numero}, foi adicionado a lista, veja como ela está: {lista}")

separador()
print("Veja a lista completa:",lista)
separador()
#1 Quantos números foram digitados:
print(f"Foram digitado: >*{len(lista)}*< números dentro da lista!")
separador()
#2 A lista de valores ordenada de forma decrescente.
lista.sort(reverse=True)
print(f"A lista ordenada de forma *decrescente*: {lista}")
separador()
#3 Se o valor 5 foi digitado e está ou não na lista.
if 5 in lista:
    print("O número *5* foi digitado e está na lista!")
else:
    print("O número *5* não foi digitado e não está na lista.")
separador()
