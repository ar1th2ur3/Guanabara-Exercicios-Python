import math

def calcularInteiro(n):
    nInteiro = math.floor(n)
    return nInteiro

def main():
    print("Desafio - 016: Crie um programa que leia um número Real qualquer pelo teclado e moastre na tela a sua parte inteira.")
    n = float(input("Digite um número: "))

    nInteiro = calcularInteiro(n)

    print(f"O número {n} tem a parte inteira {nInteiro}")

if __name__ == "__main__":
    main()
