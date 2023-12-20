def main():
    print("Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento.")

    valorProduto = float(input("Qual é o valor do produto? "))

    print("Qual seria a condição de pagamento?")

    print("1 - Á vista: dinheiro / cheque: 10 % de desconto:")
    print("2 - em até 2x no cartão: preço normal.")
    print("3 - 3x ou mais no cartão: 20% de juros.")

    opcao = int(input("Digite a opção desejada (entre 1 - 3): "))

    if opcao == 1:
        print(f"O valor do seu produto R$ {valorProduto}, irá ter 10% de desconto. Valor final: R$ {valorProduto-(valorProduto * 10)}")
    elif opcao == 2:
        print(f"Como sua escolha foi: {opcao}, o valor: R$ {valorProduto}, irá continuar o mesmo.")
    else:
        print(f"Como sua escolha foi a opção {opcao}, o valor de R$ {valorProduto} terá um acréscimo de 20% como juros. Valor final: R$ {valorProduto * 1.20:.2f}")

if __name__ == "__main__":
    main()