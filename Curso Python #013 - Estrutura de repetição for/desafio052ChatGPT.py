def is_prime(n):
    """
    Verifica se um número inteiro é primo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    # Começamos a verificar a partir de 5 em diante, pulando de 6 em 6, usando otimização.
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

def main():
    print("Este programa verifica se um número inteiro é primo ou não.")

    n_usuario = int(input("Digite um número: "))

    if is_prime(n_usuario):
        print(f"O número {n_usuario} é primo.")
    else:
        print(f"O número {n_usuario} não é primo.")

if __name__ == "__main__":
    main()
