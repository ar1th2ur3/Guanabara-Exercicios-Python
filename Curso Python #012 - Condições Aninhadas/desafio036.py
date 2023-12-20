from time import sleep

def calculoPrestaçãoMensal(valorCasa, quantidadeAnos, valorSalarioComprador):
    numero_meses = quantidadeAnos * 12  # Converte anos em meses
    valorParcela = valorCasa / numero_meses
    
    if valorParcela > 0.3 * valorSalarioComprador:
        return "Empréstimo negado"
    else:
        return valorParcela

def separator():
    print("*" * 100)

def main():
    print("Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.")
    sleep(2)
    print("O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.")
    sleep(2)
    print("Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.")
    sleep(2)
    separator()

    valorCasa = float(input("Digite o valor da Casa: "))
    quantidadeAnos = int(input("Em quantos anos o comprador planeja pagar a casa? "))
    valorSalarioComprador = float(input("Digite o salário do Comprador: "))

    valorParcela = calculoPrestaçãoMensal(valorCasa, quantidadeAnos, valorSalarioComprador)

    if valorParcela == "Empréstimo negado":
        print("Empréstimo negado. A prestação mensal excede 30% do salário do comprador.")
    else:
        print("O valor da prestação mensal é de: {:.2f}".format(valorParcela))

if __name__ == "__main__":
    main()
