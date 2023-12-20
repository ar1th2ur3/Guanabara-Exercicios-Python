def leiaint(mensagem):
    """
    Valida a entrada do usuário para garantir que seja um número inteiro.

    :param mensagem: A mensagem exibida para solicitar a entrada do usuário
    :return: Mensagem indicando se o número é inteiro ou um erro se não for
    """
    try:
        valor = int(mensagem)
        return "O seu número é um número inteiro."
    except ValueError:
        return "ERRO! DIGITE UM NÚMERO INTEIRO."

def obter_input_modo_seguro(mensagem):
    """
    Obtém a entrada do usuário de forma segura, evitando exceções.

    :param mensagem: A mensagem para solicitar a entrada do usuário
    :return: A entrada do usuário (como string)
    """
    while True:
        try:
            entrada = input(mensagem)
            break
        except KeyboardInterrupt:
            print("\nOperação interrompida pelo usuário. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Tente novamente.")

    return entrada

def main():
    """
    Função principal do programa.
    """
    print("Desafio 0104: Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico.")
    print("Exemplo: n = leiaint(Digite um número inteiro)")

    n = ""

    while not n.replace("-", "").isnumeric():
        n = obter_input_modo_seguro("Digite um número inteiro: ")
        print(leiaint(n))

if __name__ == "__main__":
    main()
