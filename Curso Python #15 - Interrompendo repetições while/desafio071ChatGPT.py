class CaixaEletronico:
    def __init__(self):
        self.cedulas = [50, 20, 10, 1]

    def sacar_valor(self, valor):
        total = valor
        resultado = {}

        for cedula in self.cedulas:
            if total >= cedula:
                resultado[cedula] = total // cedula
                total %= cedula

        return resultado


def main():
    print("Crie um programa que simule o funcionamento de um caixa eletrônico.")
    print("No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.")
    print("Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.")

    print(50 * "=")
    print("Banco Brigadeirinho.")
    print(50 * "=")

    valor_saque = int(input("Digite o valor a ser sacado: "))

    caixa = CaixaEletronico()
    resultado_saque = caixa.sacar_valor(valor_saque)

    print(50 * "=")
    print("Quantidade de cédulas entregues:")
    for cedula, quantidade in resultado_saque.items():
        print(f"{quantidade} cédula(s) de R${cedula}")

    print(50 * "=")


if __name__ == "__main__":
    main()
