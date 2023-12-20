from random import randint

def adivinhar (nRandom, nUsuario):
    if nRandom == nUsuario:
        print("Parabéns, você acertou o número!")
    else:
        print("Você errou. :)")
    return nRandom, nUsuario


def main():
    print("Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5, e peça para o usuário tentar descobrir qual foi o numero escolhido pelo computador")
    print("O programa deverá escrever na tela se o usuário venceu ou perdeu")
   
    nUsuario = int(input("Digite um número de 0 a 5 "))
    
    nRandom = randint(0,5)
    
    print("O número escolhido pelo PC foi:", nRandom)
    
    adivinhar(nRandom, nUsuario)

if __name__ == "__main__":
    main()