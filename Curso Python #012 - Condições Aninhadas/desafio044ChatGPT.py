def calcular_valor_final(valor_produto, opcao):
    if opcao == 1:
        valor_final = valor_produto - (valor_produto * 0.10)  # 10% de desconto
    elif opcao == 3:
        valor_final = valor_produto + (valor_produto * 0.20)  # 20% de juros
    else:
        valor_final = valor_produto  # Opção 2: preço normal

    return valor_final

def main():
    print("Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento.")
    
    try:
        valor_produto = float(input("Qual é o valor do produto? "))
        opcao = int(input("Digite a opção desejada (1 - À vista, 2 - 2x no cartão, 3 - 3x ou mais no cartão): "))
        
        if opcao not in (1, 2, 3):
            raise ValueError("Opção inváli10a. Escolha 1, 2 ou 3.")
        
        valor_final = calcular_valor_final(valor_produto, opcao)
        
        print(f"O valor do produto é R${valor_produto:.2f}, o valor final é R${valor_final:.2f}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
