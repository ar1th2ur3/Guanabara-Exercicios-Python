from random import randint
print("Melhore o jogo do *DESAFIO 028* onde o computador pense em um número aleatório entre 0 e 10.")
print("Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.")

numeroAleatorio = randint(1,10)
tentativas = 0

while True:
    numeroJogador = int(input("Tente adivinhar um número entre 1 - 10: "))

    if 1 <= numeroAleatorio <= 10:
        tentativas += 1

        if numeroJogador == numeroAleatorio:
            print(f"Você acertou! O número do Computador foi: {numeroAleatorio}! O total de tentativas foram: {tentativas}!")
            break
        else:
            print("Você errou, tente novamente!")
    else:
        print("Por favor, insira um número entre 1 e 10.")