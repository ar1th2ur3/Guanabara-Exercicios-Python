print("Desáfio 085: Crie um programa onde o usuário possa digitar sete valores númericos, e cadastre-os em uma lista única que mantenha separados os valores.")
print("No final, mostre os valores pares e impares em ordem crescente.")

listaTotal = []
listaPares = []
listaImpares = []


for i in range(7):
    v = int(input("Digite um valor: "))

    listaTotal.append(v)

for i in listaTotal:
    if i % 2 == 0:
        listaPares.append(i)
        listaTotal.clear
    else:
        listaImpares.append(i)
        listaTotal.clear


print("Aqui está à lista pares:", listaPares)
print("Aqui está à lista impares:", listaImpares)


