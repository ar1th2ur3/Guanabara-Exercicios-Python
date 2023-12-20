from random import randint
from time import sleep

def jogar_dado(jogador):
    resultado = randint(1, 6)
    print(f"O jogador {jogador} tirou: {resultado}")
    print("CARREGANDO...")
    sleep(1)
    return {'jogador': jogador, 'resultado': resultado}

def exibir_ranking(jogadores):
    print('-+' * 50)
    print("RANKING DOS JOGADORES")
    print('-+' * 50)
    
    for jogador in jogadores:
        print(f"Jogador {jogador['jogador']} - Pontuação: {jogador['resultado']}")
        print("CARREGANDO...")
        sleep(1)

def main():
    print("Desafio 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.")
    print("Guarde esses resultados em um dicionário.")
    print("No final, coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número no dado.")

    jogadores = []

    print('-+' * 50)

    for i in range(1, 4 + 1):
        resultado = jogar_dado(i)
        jogadores.append(resultado)

    sorted_jogadores = sorted(jogadores, key=lambda x: x['resultado'], reverse=True)
    exibir_ranking(sorted_jogadores)

if __name__ == "__main__":
    main()
