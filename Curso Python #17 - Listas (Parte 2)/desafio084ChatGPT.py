# -*- coding: utf-8 -*-

class PesquisadorRenomado:
    def __init__(self):
        self.pessoas_cadastradas = 0
        self.dados = []
        self.pessoas_pesadas = []
        self.pessoas_leves = []
        self.pessoas = []

    def cadastrar_pessoa(self):
        nome = input("Digite o nome da pessoa: ")
        peso = float(input("Digite o peso (kg) da pessoa: "))
        self.dados = [nome, peso]
        self.pessoas.append(self.dados[:])
        self.pessoas_cadastradas += 1

    def analisar_pessoas(self):
        for pessoa in self.pessoas:
            if pessoa[1] >= 50:
                self.pessoas_pesadas.append(pessoa[0])
                print(f"{pessoa[0]} é bastante pesado(a).")
            else:
                self.pessoas_leves.append(pessoa[0])
                print(f"{pessoa[0]} é bastante leve!")

    def mostrar_resultados(self):
        print(50 * "=")
        print(f"Total de pessoas cadastradas: {self.pessoas_cadastradas}")
        print(f"Pessoas mais pesadas: {', '.join(self.pessoas_pesadas)}")
        print(f"Pessoas mais leves: {', '.join(self.pessoas_leves)}")

        if self.pessoas:
            maior_peso = max(self.pessoas, key=lambda x: x[1])
            menor_peso = min(self.pessoas, key=lambda x: x[1])
            print(f"Maior peso: {maior_peso[1]} kg, de {maior_peso[0]}")
            print(f"Menor peso: {menor_peso[1]} kg, de {menor_peso[0]}")
        else:
            print("Não há pessoas cadastradas.")

if __name__ == "__main__":
    pesquisador = PesquisadorRenomado()

    print("Desafio 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.")
    print("No final, mostre:")
    print(" A) Quantas pessoas foram cadastradas.")
    print(" B) Uma listagem com as pessoas mais pesadas.")
    print(" C) Uma listagem com as pessoas mais leves.")

    for _ in range(5):
        pesquisador.cadastrar_pessoa()

    pesquisador.analisar_pessoas()
    pesquisador.mostrar_resultados()
