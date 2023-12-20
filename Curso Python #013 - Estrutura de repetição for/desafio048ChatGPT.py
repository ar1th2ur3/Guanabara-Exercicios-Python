def calcular_soma_impares_multiplos_de_tres(inicio, fim):
    if inicio < 1 or fim < inicio:
        raise ValueError("Os valores de início e fim são inválidos. O início deve ser maior ou igual a 1 e o fim deve ser maior que o início.")

    soma = 0
    numeros_impares_multiplos_de_tres = []

    for numero in range(inicio, fim + 1):
        if numero % 3 == 0 and numero % 2 != 0:
            numeros_impares_multiplos_de_tres.append(numero)
            soma += numero

    return numeros_impares_multiplos_de_tres, soma

def imprimir_numeros_impares_multiplos_de_tres(numeros):
    print("Números ímpares e múltiplos de três no intervalo:")
    for numero in numeros:
        print(numero)

def main():
    print("Este programa calcula a soma de todos os números ímpares que são múltiplos de três no intervalo de 1 até um valor de sua escolha.")

    try:
        inicio = int(input("Informe o valor de início (deve ser maior ou igual a 1): "))
        fim = int(input("Informe o valor de fim (deve ser maior que o início): "))

        numeros_impares, soma = calcular_soma_impares_multiplos_de_tres(inicio, fim)

        imprimir_numeros_impares_multiplos_de_tres(numeros_impares)
        print(f"A soma dos números é: {soma}")

    except ValueError as ve:
        print(f"Erro: {ve}")
    except ValueError as ve:
        print(f"Erro: {ve}")

if __name__ == "__main__":
    main()
