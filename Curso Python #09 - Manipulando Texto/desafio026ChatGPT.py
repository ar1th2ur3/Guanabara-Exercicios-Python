def contar_letra_a(frase):
    """Conta quantas vezes a letra 'a' aparece na frase."""
    return frase.lower().count('a')  # Usamos lower() para contar 'a' e 'A' como a mesma letra.

def primeira_ocorrencia(frase):
    """Retorna a posição da primeira ocorrência da letra 'a' na frase ou -1 se não encontrada."""
    return frase.lower().find('a')

def ultima_ocorrencia(frase):
    """Retorna a posição da última ocorrência da letra 'a' na frase ou -1 se não encontrada."""
    return frase.lower().rfind('a')

def main():
    print("Faça um programa que leia uma frase pelo teclado e mostre:")
    print("1- Quantas vezes aparece a letra 'a'")
    print("2- Em que posição ela aparece a primeira vez")
    print("3- Em que posição ela aparece a última vez")

    frase = input("Digite uma frase: ")

    # 1. Conta quantas vezes a letra 'a' aparece
    quantidade_a = contar_letra_a(frase)
    print(f"A letra 'a' aparece {quantidade_a} vezes na sua frase.")

    # 2. Encontra a posição da primeira ocorrência da letra 'a'
    primeira_posicao = primeira_ocorrencia(frase)
    if primeira_posicao != -1:
        print(f"A primeira vez que a letra 'a' aparece está no índice {primeira_posicao}.")
    else:
        print("A letra 'a' não foi encontrada na frase.")

    # 3. Encontra a posição da última ocorrência da letra 'a'
    ultima_posicao = ultima_ocorrencia(frase)
    if ultima_posicao != -1:
        print(f"A última vez que a letra 'a' aparece está no índice {ultima_posicao}.")
    else:
        print("A letra 'a' não foi encontrada na frase.")

if __name__ == "__main__":
    main()
