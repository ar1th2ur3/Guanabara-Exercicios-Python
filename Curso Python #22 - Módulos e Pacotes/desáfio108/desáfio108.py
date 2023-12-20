import moeda

print("Desáfio 108: Adapte o código do desáfio 0107, criando uma função adicional chamada moeda(), que consiga mostrar os valores como um valor monetário formatado.")
numero = int(input("Digite um número: "))

print(f"O dobro de {numero} é: {moeda.moeda(moeda.dobro(numero))}")
print(f"A metade de: {numero} é: {moeda.moeda(moeda.metade(numero))}")
print(f"Aumentando 10%, temos: {moeda.moeda(moeda.aumentar(numero,10))}")
print(f"Diminuindo 10%, temos: {moeda.moeda(moeda.diminuir(numero,10))}")
print(f"O número formatado é: {moeda.moeda(numero)}")