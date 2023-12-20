def calcular_soma_pares(numeros):
    """
    Calcula a soma dos números pares em uma lista de números.

    Args:
        numeros (list): Uma lista de números inteiros.

    Returns:
        int: A soma dos números pares na lista.
    """
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    return soma

def main():
    print("Este programa lê seis números inteiros e calcula a soma dos números pares. Números ímpares são desconsiderados.")

    numeros = []
    for i in range(1, 7):
        try:
            numero = int(input(f"Digite o {i}º número: "))
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    soma_pares = calcular_soma_pares(numeros)

    print(f"A soma dos números pares é: {soma_pares}")

if __name__ == "__main__":
    main()
