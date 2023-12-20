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
                print(f"Adicionando o valor {valor} à posição ({i+1}, {j+1}) da matriz.")
                self.matriz[i][j] = valor

    def mostrar_matriz(self):
        print("\n=== Matriz Resultante ===")
        print(50 * "=")

        for linha in self.matriz:
            print(linha)

        print(50 * "=")
        print("Matriz formatada exibida na tela.")

if __name__ == "__main__":
    pesquisador = PesquisadorRenomado()

    print("Desafio 086: Crie um programa que crie uma matriz de dimensão 3x3.")
    print("Preencha com valores lidos pelo teclado.")
    print("No final, mostre a matriz na tela, com a formatação correta.")

    pesquisador.preencher_matriz()
    pesquisador.mostrar_matriz()
