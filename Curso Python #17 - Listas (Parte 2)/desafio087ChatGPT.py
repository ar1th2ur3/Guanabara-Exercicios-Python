# -*- coding: utf-8 -*-

class PesquisadorRenomado:
    def __init__(self):
        self.matriz = [[0, 0, 0] for _ in range(3)]

    def preencher_matriz(self):
        print("\n=== Preenchimento da Matriz ===")
        for i in range(3):
            print(f"\nLinha {i+1}:")
            for j in range(3):
                valor = int(input(f"  Digite um número para a posição ({i+1}, {j+1}): "))
                self.matriz[i][j] = valor

    def mostrar_matriz(self):
        print("\n=== Matriz Resultante ===")
        print(50 * "=")
        for linha in self.matriz:
            print(linha)
        print(50 * "=")

    def calcular_somas(self):
        soma_pares = 0
        soma_terceira_coluna = 0
        maior_segunda_linha = max(self.matriz[1])

        for i in range(3):
            for j in range(3):
                if self.matriz[i][j] % 2 == 0:
                    soma_pares += self.matriz[i][j]

                if j == 2:
                    soma_terceira_coluna += self.matriz[i][j]

        print(f"Soma dos valores pares: {soma_pares}")
        print(f"Soma dos valores da terceira coluna: {soma_terceira_coluna}")
        print(f"Maior valor da segunda linha: {maior_segunda_linha}")


if __name__ == "__main__":
    pesquisador = PesquisadorRenomado()

    print("Desafio 087: Aprimore o desafio anterior, mostrando no final:")
    print("A) A soma de todos os valores pares digitados.")
    print("B) A soma dos valores da terceira coluna.")
    print("C) O maior valor da segunda linha.")

    pesquisador.preencher_matriz()
    pesquisador.mostrar_matriz()
    pesquisador.calcular_somas()
