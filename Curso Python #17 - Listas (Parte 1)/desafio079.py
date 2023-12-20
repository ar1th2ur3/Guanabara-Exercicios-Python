def separador():
    print(50 * "=")

print("Desáfio 079: Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. ")
separador()
print("Caso o número já existe lá dentro, ele não será adicionado.")
separador()
print("No final, serão exibidos todos os valores únicos digitados em ordem crescente.")
separador()

l = []

for i in range(0,10):
    v = int(input("Digite o valor desejado: "))
    if v in l:
        print(f"O número: {v} já está na lista, então ele não será adicionado.")
        continue
    else:
         l.append(v)  
         
print(sorted(l))