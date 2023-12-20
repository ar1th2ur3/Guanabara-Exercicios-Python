def ficha(nome="<desconhecido>", gols=0):
    """
    Função que exibe a ficha de um jogador.

    :param nome: Nome do jogador (opcional, default é "<desconhecido>")
    :param gols: Número de gols do jogador (opcional, default é 0)
    :return: String contendo a ficha do jogador
    """
    if not nome.strip():  # Verifica se o nome é vazio ou contém apenas espaços em branco
        nome = "<desconhecido>"

    try:
        gols = int(gols)  # Tenta converter a entrada dos gols para um número inteiro
    except ValueError:
        gols = 0  # Atribui 0 se a conversão falhar

    return f"O jogador {nome} fez {gols} gol(s) no campeonato."

def obter_input_modo_seguro(mensagem):
    """
    Função para obter entrada do usuário de forma segura, evitando exceções.

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

print("Desafio 103: Faça um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.")
print("O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.")

nomeJogador = obter_input_modo_seguro("Qual o nome do Jogador? ")
golsJogador = obter_input_modo_seguro(f"Quantos gols o jogador {nomeJogador} fez? ")

print(ficha(nomeJogador, golsJogador))
