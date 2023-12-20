# Importar a biblioteca de tempo para usar sleep
from time import sleep

# Função para calcular a prestação mensal
def calculoPrestaçãoMensal(valorCasa, quantidadeAnos, valorSalarioComprador):
    # Converter anos em meses
    numero_meses = quantidadeAnos * 12
    # Calcular o valor da parcela
    valorParcela = valorCasa / numero_meses
    
    # Verificar a elegibilidade do empréstimo
    if valorParcela > 0.3 * valorSalarioComprador:
        return "Empréstimo negado"
    else:
        return valorParcela

# Função para imprimir uma linha de separação
def separator():
    print("*" * 100)

# Função principal
def main():
    # Apresentação do programa
    print("Este programa avalia a aprovação de empréstimos bancários para a compra de casas.")
    sleep(2)
    print("Ele coletará informações sobre o valor da casa, o salário do comprador e o prazo do empréstimo.")
    sleep(2)
    print("Em seguida, calculará a prestação mensal, que não deve exceder 30% do salário para ser aprovada.")
    sleep(2)
    separator()

    # Coleta de informações do usuário
    valorCasa = float(input("Digite o valor da Casa: "))
    quantidadeAnos = int(input("Em quantos anos o comprador planeja pagar a casa? "))
    valorSalarioComprador = float(input("Digite o salário do Comprador: "))

    # Cálculo da prestação mensal
    valorParcela = calculoPrestaçãoMensal(valorCasa, quantidadeAnos, valorSalarioComprador)

    # Verificação de elegibilidade e exibição de resultados
    if valorParcela == "Empréstimo negado":
        print("Empréstimo negado. A prestação mensal excede 30% do salário do comprador.")
    else:
        print(f"O valor da prestação mensal é de: R${valorParcela:.2f}")

if __name__ == "__main__":
    main()
