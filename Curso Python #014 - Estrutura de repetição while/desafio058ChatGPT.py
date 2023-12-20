from random import randint

# Introdução do jogo
print("Jogo de Adivinhação - Desafio para a Diretoria")
print("Neste jogo, o computador pensará em um número entre 1 e 10.")
print("Seu objetivo é adivinhar o número com o menor número de tentativas possíveis.")
print("Boa sorte!\n")

# Geração do número aleatório
numeroAleatorio = randint(1, 10)
tentativas = 0

# Início do loop do jogo
while True:
    # Entrada do jogador e validação
    while True:
        try:
            numeroJogador = int(input("Tente adivinhar um número (de 1 a 10): "))
            if 1 <= numeroJogador <= 10:
                break
            else:
                print("Por favor, insira um número dentro do intervalo permitido.")
        except ValueError:
            print("Por favor, insira um número válido.")
    
    # Contagem de tentativas
    tentativas += 1
    
    # Verificação se o jogador acertou
    if numeroJogador == numeroAleatorio:
        print(f"Parabéns! Você acertou. O número do computador era: {numeroAleatorio}")
        print(f"Total de tentativas: {tentativas}\n")
        break
    else:
        print("Você errou. Tente novamente!\n")

# Agradecimento e encerramento do jogo
print("O jogo terminou. Obrigado por jogar!")
