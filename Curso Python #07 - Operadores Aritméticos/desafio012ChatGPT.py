def calcular_valor_com_desconto(valor, desconto_percentual):
    valor_desconto = valor * (desconto_percentual / 100)
    valor_com_desconto = valor - valor_desconto
    return valor_com_desconto

def main():
    print("Calculadora de desconto de produto")

    valor_produto = float(input("Digite o valor do produto em reais: "))
    desconto_percentual = 5  # 5% de desconto

    valor_com_desconto = calcular_valor_com_desconto(valor_produto, desconto_percentual)

    print(f"O produto custa R${valor_produto:.2f}, e com {desconto_percentual}% de desconto, ele custa R${valor_com_desconto:.2f}.")

if __name__ == "__main__":
    main()
