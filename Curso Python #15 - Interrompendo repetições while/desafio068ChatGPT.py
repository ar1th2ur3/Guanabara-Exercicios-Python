from random import randint

print("Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no jogo.")

print(50 * "===", "\nVAMOS JOGAR PAR OU IMPAR ?", "\n" + 50 * "===")

nContador = 0

while True:
    try:
        nComputador = randint(1, 10)
        nJogador = int(input("Escolha um número: "))
        escolhaJogador = str(input("Escolha P ou I: ")).lower()
        print(f"A escolha do Computador foi: {nComputador}")

        resultado = nComputador + nJogador

        if escolhaJogador == "p":
            if resultado % 2 == 0:
                print("Você venceu, parabéns!")
                nContador += 1
                print(f"Você tem {nContador} pontos!")
            else:
                print("Você perdeu. :(")
                break
        elif escolhaJogador == "i":
            if resultado % 2 != 0:
                print("Você venceu, parabéns!")
                nContador += 1
                print(f"Você tem {nContador} pontos!")
            else:
                print("Você perdeu. :(")
                break
        else:
            print("Escolha inválida. Por favor, digite P ou I.")
    except ValueError:
        print("Por favor, digite um número válido.")
