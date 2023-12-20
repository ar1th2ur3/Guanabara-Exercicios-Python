from random import randint

def verificar_par_impar(numero):
    """
    Função que verifica se um número é par ou ímpar.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        str: Uma mensagem indicando se o número é par ou ímpar.
    """
    if numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

def main():
    print("Bem-vindo ao desafio de verificar par ou ímpar!")
    print("Este programa lê um número inteiro e determina se ele é par ou ímpar.")

    numero = randint(0, 1000)  # Gere um número aleatório para demonstração.

    mensagem = verificar_par_impar(numero)
    print(f"O número {numero} é {mensagem}")

if __name__ == "__main__":
    main()
