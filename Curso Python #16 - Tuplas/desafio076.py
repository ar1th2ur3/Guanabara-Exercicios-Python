print("Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.")
print("No final, mostre uma lista de preços organizando os dados em forma tabular.")

t = ("Laranja", 2.5, "Abacaxi", 3.0, "Maçã", 2.0, "Uva", 4.5, "Pera", 3.2)

for i in range(0, len(t), 2):
    nome_produto = t[i]
    preco_produto = t[i + 1]
    print(f"O nome do produto é: {nome_produto}......Valor: R$ {preco_produto}")
