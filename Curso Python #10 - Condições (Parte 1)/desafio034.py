import time
def calculoAumento(vSalario):
    if vSalario > 1250:
        novo_salario = vSalario * 1.10
        return f"Seu salário será aumentado em 10% e será de R${novo_salario:.2f}."
    else:
        novo_salario = vSalario * 1.15
        return f"Seu salário será aumentado em 15% e será de R${novo_salario:.2f}"

def main():
    print("Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.")
    time.sleep(2)
    print("Para salários superiores a R$1.250, calcule um aumento de 10%.")
    time.sleep(2)
    print("Para salários iguais ou inferiores, o aumento é de 15%.")
    time.sleep(2)

    vSalario = float(input("Digite o seu salário: "))
    time.sleep(2)

    mensagem = calculoAumento(vSalario)

    print(mensagem)

if __name__ == "__main__":
    main()
