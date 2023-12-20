# -*- coding: utf-8 -*-

class PesquisadorRenomado:
    def __init__(self):
        self.lista_total = []
        self.lista_pares = []
        self.lista_impares = []

    def cadastrar_valores(self):
        for _ in range(7):
            valor = int(input("Digite um valor: "))
            self.lista_total.append(valor)

    def separar_pares_impares(self):
        for valor in self.lista_total:
            if valor % 2 == 0:
                self.lista_pares.append(valor)
            else:
                self.lista_impares.append(valor)

    def mostrar_resultados(self):
        self.lista_pares.sort()
        self.lista_impares.sort()

        print("Valores pares em ordem crescente:", self.lista_pares)
        print("Valores ímpares em ordem crescente:", self.lista_impares)

if __name__ == "__main__":
    pesquisador = PesquisadorRenomado()

    print("Desafio 085: Crie um programa onde o usuário possa digitar sete valores numéricos, e cadastre-os em uma lista única que mantenha separados os valores.")
    print("No final, mostre os valores pares e ímpares em ordem crescente.")

    pesquisador.cadastrar_valores()
    pesquisador.separar_pares_impares()
    pesquisador.mostrar_resultados()
