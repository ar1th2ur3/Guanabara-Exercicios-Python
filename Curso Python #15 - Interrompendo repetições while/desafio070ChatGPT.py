class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    while True:
        try:
            preco = float(input("Digite o preço do produto: R$"))
            break
        except ValueError:
            print("Por favor, digite um valor numérico para o preço.")
    return Produto(nome, preco)


def main():
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

    lista_produtos = []

    while True:
        produto = cadastrar_produto()
        lista_produtos.append(produto)

        escolha = input("Você quer continuar? [SIM / NÃO] ").lower()
        if escolha != "sim":
            break

    if lista_produtos:
        total_valor_produto = sum(produto.preco for produto in lista_produtos)
        quantidade_produtos_1000 = sum(1 for produto in lista_produtos if produto.preco > 1000)
        produto_mais_barato = min(lista_produtos, key=lambda x: x.preco)

        print(50 * "=")
        print(f"O valor total do produto é: R${total_valor_produto:.2f}")
        print(50 * "=")
        print(f"Temos {quantidade_produtos_1000} produtos custando mais de R$1000.")
        print(50 * "=")
        print(f"O nome do produto mais barato é: {produto_mais_barato.nome} e o seu valor é: R${produto_mais_barato.preco:.2f}")
    else:
        print("Nenhum produto foi cadastrado.")


if __name__ == "__main__":
    main()
