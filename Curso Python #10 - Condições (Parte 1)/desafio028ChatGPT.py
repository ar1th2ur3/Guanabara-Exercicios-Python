import random

def adivinhar(nRandom, nUsuario):
    if nRandom == nUsuario:
        return "Parabéns, você acertou o número!"
    else:
        return "Você errou. :("

def main():
    print("Bem-vindo ao desafio de adivinhação!")
    print("O computador escolheu um número inteiro entre 0 e 5. Tente adivinhar qual é!")

    while True:
        nRandom = random.randint(0, 5)
        nUsuario = int(input("Digite um número de 0 a 5: "))

        resultado = adivinhar(nRandom, nUsuario)
        print("O número escolhido pelo computador foi:", nRandom)
        print(resultado)

        jogar_novamente = input("Deseja jogar novamente? (S para Sim, qualquer outra tecla para sair): ")
        if jogar_novamente.lower() != 's':
            break

if __name__ == "__main__":
    main()
