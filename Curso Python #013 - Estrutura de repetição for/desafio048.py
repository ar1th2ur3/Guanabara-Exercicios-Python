def calculo_impar(contador):
    soma = 0  # Inicializamos uma variável para armazenar a soma dos números ímpares múltiplos de três
    for c in range(1, contador + 1):  # Começamos a partir de 1 e incluímos o valor de contador
        if c % 3 == 0 and c % 2 != 0:  # Verificamos se o número é ímpar e múltiplo de três
            print(c)  # Imprimimos o número ímpar e múltiplo de três
            soma += c  # Adicionamos o número à soma
    return soma  # Retornamos a soma

def main():
    print("Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.")

    total = calculo_impar(500)  # Chamamos a função calculo_impar para calcular a soma

    print(f"O total é: {total}")  # Exibimos o resultado da soma

if __name__ == "__main__":
    main()
