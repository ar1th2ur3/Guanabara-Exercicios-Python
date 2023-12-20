print("Crie um programa que leia o nome e o preço de vários produtos.")
print("O programa deverá perguntar se o usuário vai continuar.")
print("No final, mostre: ")
print(50 * "*")
print("A) Qual é o total gasto na compra.")
print(50 * "*")
print("B) Quantos produtos custam mais de R$1000")
print(50 * "*")
print("C) Qual é o nome do produto mais barato.")
print(50 * "*")

lista = []
total_valor_produto = quantidade_produtos_1000 = 0

while True:
    nome_produto = str(input("Qual é o nome do produto? "))
    
    try:
        preco_produto = float(input("Qual é o preço do produto? "))
    except ValueError:
        print("Por favor, digite um valor numérico para o preço.")
        continue

    if preco_produto > 1000:
        quantidade_produtos_1000 += 1

    total_valor_produto += preco_produto

    lista.append({"nome": nome_produto, "preco": preco_produto})

    escolha = str(input("Você quer continuar? [SIM / NÃO] ")).lower()

    if escolha != "sim":
        break

# Busca pelo produto mais barato após a entrada dos produtos
if lista:
    produto_mais_barato = min(lista, key=lambda x: x["preco"])
    
    print(50 * "=")
    print(f"O valor total do produto é: R${total_valor_produto}")
    print(50 * "=")
    print(f"Temos {quantidade_produtos_1000} produtos custando mais de R$1000.")
    print(50 * "=")
    print(f"O nome do produto mais barato é: {produto_mais_barato['nome']} e o seu valor é: R${produto_mais_barato['preco']}")
else:
    print("Nenhum produto foi cadastrado.")
