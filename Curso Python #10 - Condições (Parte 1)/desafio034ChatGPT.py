def calculoAumento(vSalario, tipo_aumento):
    if tipo_aumento == "10%":
        novo_salario = vSalario * 1.10
        return f"Seu salário será aumentado em 10% e será de R${novo_salario:.2f}."
    elif tipo_aumento == "15%":
        novo_salario = vSalario * 1.15
        return f"Seu salário será aumentado em 15% e será de R${novo_salario:.2f}."
    else:
        return "Opção de aumento inválida."

def main():
    print("Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do aumento.")
    print("Escolha o tipo de aumento: 10% ou 15%.")

    vSalario = float(input("Digite o seu salário: "))
    tipo_aumento = input("Escolha o tipo de aumento (10% ou 15%): ")

    mensagem = calculoAumento(vSalario, tipo_aumento)

    print(mensagem)

if __name__ == "__main__":
    main()
