def leiaint(mensagem):
    """
    Valida a entrada do usuário para garantir que seja um número inteiro.

    :param mensagem: A mensagem exibida para solicitar a entrada do usuário
    :return: Mensagem indicando se o número é inteiro ou um erro se não for
    """
    if mensagem.isnumeric():
        return "O seu número é um número inteiro."
    else:
        return "ERRO! DIGITE UM NÚMERO INTEIRO."

n = ""

while n.isnumeric() == False:
    n = str(input("Digite um número inteiro: "))
    print(leiaint(n))
