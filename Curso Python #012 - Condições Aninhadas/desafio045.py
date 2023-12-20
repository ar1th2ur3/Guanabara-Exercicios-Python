import random

def main():
    print("Crie um programa que faça o computador jogar Jokenpô com você.")

    palavras = ["pedra", "papel","tesoura"]

    jogadorEscolha = str(input("Faça sua jogada (escolha entre: pedra, papel ou tesoura.): "))

    computadorEscolha = random.choice(palavras)

    print(f"A escolha do Computador foi: {computadorEscolha}")

    if jogadorEscolha == "papel" and computadorEscolha == "papel":
        print("Empate!")
    elif jogadorEscolha == "pedra" and computadorEscolha == "pedra":
        print("Empate!")
    elif jogadorEscolha == "tesoura" and computadorEscolha == "tesoura":
        print("Empate!")
    elif jogadorEscolha == "pedra" and computadorEscolha == "papel":
        print("O Computador ganhou!")
    elif jogadorEscolha == "papel" and computadorEscolha == "tesoura":
        print("O Computador ganhour!")
    elif jogadorEscolha == "tesoura" and computadorEscolha == "pedra":
        print("Computador ganhou!")
    elif computadorEscolha == "pedra" and jogadorEscolha == "papel":
        print("O Jogador ganhou!")
    elif computadorEscolha == "papel" and jogadorEscolha == "tesoura":
        print("O Jogador ganhou!")
    elif computadorEscolha == "tesoura" and jogadorEscolha == "pedra":
        print("O Jogador ganhou!")


if __name__ == "__main__":
    main()
    while True:
        main()

        jogarNovamente = input("Você deseja jogar novamente ? Digite Sim ou Não.")
        if jogarNovamente != "sim":
            break
