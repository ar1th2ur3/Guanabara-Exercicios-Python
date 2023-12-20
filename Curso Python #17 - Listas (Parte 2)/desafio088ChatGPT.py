from random import randint
from time import sleep

class PesquisadorRenomado:
    def __init__(self):
        self.jogos = []

    def gerar_palpites(self, quantidade):
        print(f"=== SORTEANDO {quantidade} JOGOS ===")
        for _ in range(quantidade):
            jogo = self.sortear_numeros()
            self.jogos.append(jogo)
            print(f"Jogo {len(self.jogos)}: {jogo}")
            sleep(1)

    def sortear_numeros(self):
        numeros_sorteados = []
        for _ in range(6):
            numero = randint(1, 60)
            while numero in numeros_sorteados:
                numero = randint(1, 60)
            numeros_sorteados.append(numero)
        return sorted(numeros_sorteados)

if __name__ == "__main__":
    pesquisador = PesquisadorRenomado()

    print("Desafio 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.")
    print("O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.")

    quantidade_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
    pesquisador.gerar_palpites(quantidade_jogos)
