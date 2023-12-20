import random
from colorama import Fore, Style, init

init(autoreset=True)

def jogar_jokenpo():
    pontuacao_jogador = 0
    pontuacao_computador = 0

    while True:
        print(Fore.CYAN + "Bem-vindo ao Jokenpô!" + Style.RESET_ALL)

        opcoes = ["pedra", "papel", "tesoura"]
        jogador_escolha = input(Fore.YELLOW + "Faça sua jogada (escolha entre: pedra, papel ou tesoura): " + Style.RESET_ALL).lower()

        if jogador_escolha not in opcoes:
            print(Fore.RED + "Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura." + Style.RESET_ALL)
            continue

        computador_escolha = random.choice(opcoes)
        print(Fore.MAGENTA + f"A escolha do Computador foi: {computador_escolha}" + Style.RESET_ALL)

        if jogador_escolha == computador_escolha:
            print(Fore.YELLOW + "Empate!" + Style.RESET_ALL)
        elif (jogador_escolha == "pedra" and computador_escolha == "tesoura") or \
             (jogador_escolha == "papel" and computador_escolha == "pedra") or \
             (jogador_escolha == "tesoura" and computador_escolha == "papel"):
            print(Fore.GREEN + "Você ganhou!" + Style.RESET_ALL)
            pontuacao_jogador += 1
        else:
            print(Fore.RED + "O Computador ganhou!" + Style.RESET_ALL)
            pontuacao_computador += 1

        print(Fore.CYAN + f"Pontuação - Jogador: {pontuacao_jogador}, Computador: {pontuacao_computador}" + Style.RESET_ALL)

        jogar_novamente = input(Fore.CYAN + "Deseja jogar novamente? (Digite 'sim' para continuar ou qualquer outra coisa para sair): " + Style.RESET_ALL).lower()
        if jogar_novamente != 'sim':
            break

def main():
    print(Fore.YELLOW + "Crie um programa que faça o computador jogar Jokenpô com você." + Style.RESET_ALL)
    jogar_jokenpo()

if __name__ == "__main__":
    main()
