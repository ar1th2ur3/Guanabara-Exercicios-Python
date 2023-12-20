from random import randint

print("Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquiestou no jogo.")

print(50 * "===")
print("VAMOS JOGAR PAR OU IMPAR ?")
print(50 * "===")

nComputador = randint(1,10)
nContador = 0

while True: 

    nJogador = int(input("Escolha um número: "))
    escolhaJogador = str(input("Escolha P ou I: ")).lower()
    print(f"A escolha do Computador foi: {nComputador}")

    resultado = nComputador + nJogador

    if escolhaJogador == "P":
        if resultado % 2 == 0:
            print("Você venceu, parabéns!")
            print("Vamos jogar novamente!")
            nContador += 1
            print(f"Você tem {nContador} pontos!")
    elif escolhaJogador == "I":
        if resultado % 2 != 0:
            print("Você venceu, parabéns!")
            print("Vamos jogar novamente!")
    else:
        print("Você perdeu. :( ")
        break