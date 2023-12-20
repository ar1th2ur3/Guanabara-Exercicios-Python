import moeda

print("Desáfio 0107: Crie um módulo chamado moeda.py que tenhas as funções incorporadas: aumentar(), diminuir(),dobro() e metade().")
print("Faça também um programa que importe esse módulo e use algumas dessas funções")

numero = int(input("Digite um número: "))

print(f"O dobro de {numero} é: {moeda.moeda(moeda.dobro(numero))}")
print(f"A metade de: {numero} é: {moeda.moeda(moeda.metade(numero))}")
print(f"Aumentando 10%, temos: {moeda.moeda(moeda.aumentar(numero,10))}")
print(f"Diminuindo 10%, temos: {moeda.moeda(moeda.diminuir(numero,10))}")
print(f"O número formatado é: {moeda.moeda(numero)}")