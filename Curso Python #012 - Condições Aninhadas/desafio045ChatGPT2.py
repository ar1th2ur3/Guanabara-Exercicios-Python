import random
from colorama import Fore, Style, init

init(autoreset=True)

def jogar_jokenpgadores):
    pontuacoes = {f"Jogo(num_joador {i}": 0 for i in range(1, num_jogadores + 1)}

    while True:
        print(Fore.CYAN + "Bem-vindo ao Jokenpô!" + Style.RESET_ALL)

        opcoes = ["pedra", "papel", "tesoura"]

        for i in range(1, num_jogadores + 1):
            jogador_escolha = input(Fore.YELLOW + f"Jogador {i}, faça sua jogada (escolha entre: pedra, papel ou tesoura): " + Style.RESET_ALL).lower()

            if jogador_escolha not in opcoes:
                print(Fore.RED + "Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura." + Style.RESET_ALL)
                continue

            computador_escolha = random.choice(opcoes)
            print(Fore.MAGENTA + f"A escolha do Computador foi: {computador_escolha}" + Style.RESET_ALL)

            if jogador_escolha == computador_escolha:
                print(Fore.YELLOW + f"Jogador {i}: Empate!" + Style.RESET_ALL)
            elif (jogador_escolha == "pedra" and computador_escolha == "tesoura") or \
                 (jogador_escolha == "papel" and computador_escolha == "pedra") or \
                 (jogador_escolha == "tesoura" and computador_escolha == "papel"):
                print(Fore.GREEN + f"Jogador {i}: Você ganhou!" + Style.RESET_ALL)
                pontuacoes[f"Jogador {i}"] += 1
            else:
                print(Fore.RED + f"Jogador {i}: O Computador ganhou!" + Style.RESET_ALL)

        print(Fore.CYAN + "Pontuações:" + Style.RESET_ALL)
        for jogador, pontuacao in pontuacoes.items():
            print(Fore.CYAN + f"{jogador}: {pontuacao} pontos" + Style.RESET_ALL)

        jogar_novamente = input(Fore.CYAN + "Deseja jogar novamente? (Digite 'sim' para continuar ou qualquer outra coisa para sair): " + Style.RESET_ALL).lower()
        if jogar_novamente != 'sim':
            break

def main():
    print(Fore.YELLOW + "Crie um programa que faça o computador jogar Jokenpô com você." + Style.RESET_ALL)
    
    num_jogadores = int(input(Fore.YELLOW + "Quantos jogadores participarão da partida? " + Style.RESET_ALL))
    jogar_jokenpo(num_jogadores)

if __name__ == "__main__":
    main()
