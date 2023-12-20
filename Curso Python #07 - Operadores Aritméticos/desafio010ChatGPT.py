def calcular_quantidade_de_dolares(valor_em_reais, taxa_de_cambio=3.27):
    """
    Calcula a quantidade de dólares que podem ser comprados com base em um valor em reais.

    :param valor_em_reais: O valor em reais que você deseja converter para dólares.
    :param taxa_de_cambio: A taxa de câmbio atual (por padrão, 3.27 reais por dólar).
    :return: A quantidade de dólares que podem ser comprados.
    """
    quantidade_de_dolares = valor_em_reais / taxa_de_cambio
    return quantidade_de_dolares

def main():
    print("Calculadora de conversão de Reais para Dólares")
    valor_em_reais = float(input("Digite o total de dinheiro que você possui em reais: "))
    
    quantidade_de_dolares = calcular_quantidade_de_dolares(valor_em_reais)
    
    print(f"Com R${valor_em_reais:.2f}, você pode comprar ${quantidade_de_dolares:.2f} dólares.")

if __name__ == "__main__":
    main()
