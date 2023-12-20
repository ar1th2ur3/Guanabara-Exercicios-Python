def calcular_progressao_aritmetica(primeiro_termo, razao, quantidade_termos):
    termos = []

    for i in range(quantidade_termos):
        termo = primeiro_termo + i * razao
        termos.append(termo)

    return termos

def exibir_progressao_aritmetica(termos):
    print("Termos da progressão aritmética:")
    for i, termo in enumerate(termos, start=1):
        print(f"Termo {i}: {termo}")

def main():
    print("Este programa calcula e exibe os primeiros termos de uma progressão aritmética.")

    try:
        primeiro_termo = int(input("Digite o primeiro termo da progressão: "))
        razao = int(input("Digite a razão da progressão: "))
        quantidade_termos = 10  # Mostrar os 10 primeiros termos por padrão

        termos = calcular_progressao_aritmetica(primeiro_termo, razao, quantidade_termos)
        exibir_progressao_aritmetica(termos)

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
def calcular_progressao_aritmetica(primeiro_termo, razao, quantidade_termos):
    termos = []

    for i in range(quantidade_termos):
        termo = primeiro_termo + i * razao
        termos.append(termo)

    return termos

def exibir_progressao_aritmetica(termos):
    print("Termos da progressão aritmética:")
    for i, termo in enumerate(termos, start=1):
        print(f"Termo {i}: {termo}")

def main():
    print("Este programa calcula e exibe os primeiros termos de uma progressão aritmética.")

    try:
        primeiro_termo = int(input("Digite o primeiro termo da progressão: "))
        razao = int(input("Digite a razão da progressão: "))
        quantidade_termos = 10  # Mostrar os 10 primeiros termos por padrão

        termos = calcular_progressao_aritmetica(primeiro_termo, razao, quantidade_termos)
        exibir_progressao_aritmetica(termos)

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
