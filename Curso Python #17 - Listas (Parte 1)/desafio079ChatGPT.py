class DesafioProgram:
    def __init__(self):
        self.valores = []

    def separador(self):
        print(50 * "=")

    def obter_valores(self, quantidade=10):
        for _ in range(quantidade):
            try:
                valor = int(input("Digite o valor desejado: "))
                self.adicionar_valor(valor)
            except ValueError:
                print("Por favor, insira um valor numérico válido.")

    def adicionar_valor(self, valor):
        if valor in self.valores:
            print(f"O número {valor} já está na lista e não será adicionado.")
        else:
            self.valores.append(valor)

    def exibir_valores_unicos(self):
        self.separador()
        print("Valores únicos digitados em ordem crescente:")
        print(sorted(self.valores))
        self.separador()

if __name__ == "__main__":
    programa = DesafioProgram()

    print("Desafio 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.")
    programa.separador()
    print("Caso o número já exista na lista, ele não será adicionado.")
    programa.separador()
    print("No final, serão exibidos todos os valores únicos digitados em ordem crescente.")
    programa.separador()

    programa.obter_valores()

    programa.exibir_valores_unicos()
