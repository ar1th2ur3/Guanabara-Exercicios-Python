from random import randint

def verificar(n):
    if n % 2 == 0:
        mensagem = "par."
    else:
        mensagem = "ímpar."
    return mensagem

def main():
    print("Desafio 030: Leia um programa que leia um número inteiro qualquer e mostre na tela se ele é par ou ímpar")
    n = randint(0, 1000)  # Gere um número aleatório para testar

    mensagem = verificar(n)
    print(f"O número {n} é {mensagem}")

if __name__ == "__main__":
    main()
