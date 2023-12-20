def ficha(nome, gols):
    """
    Exibe a ficha do jogador.

    :param nome: Nome do jogador (opcional, default é "<desconhecido>")
    :param gols: Número de gols do jogador (opcional, default é 0)
    :return: String contendo a ficha do jogador
    """
    # Verifica se tanto o nome quanto os gols estão vazios
    if nome == "" and gols == "":
        nome = "<desconhecido>"  # Se ambos estiverem vazios, atribui "<desconhecido>" ao nome
        gols = 0  # Se ambos estiverem vazios, atribui 0 aos gols
        return f"O jogador {nome} fez {gols} gol(s) no campeonato!"

    # Verifica se apenas os gols estão vazios
    elif gols == "":
        gols = 0  # Se apenas os gols estiverem vazios, atribui 0 aos gols
        return f"O jogador {nome} fez {gols} gol(s) no campeonato!"

    # Verifica se apenas o nome está vazio
    elif nome == "":
        nome = "<desconhecido>"  # Se apenas o nome estiver vazio, atribui "<desconhecido>" ao nome
        return f"O jogador {nome} fez {gols} gol(s) no campeonato!"

    # Se nenhum dos casos anteriores for verdadeiro, retorna a ficha do jogador com os valores fornecidos
    else:
        return f"O jogador {nome} fez {gols} gol(s) no campeonato!"

# Solicita o nome e os gols do jogador ao usuário
nomeJogador = str(input("Qual o nome do Jogador? "))
golsJogador = str(input(f"Quantos gols o jogador {nomeJogador} fez? "))

# Chama a função ficha com os valores fornecidos e exibe o resultado
print(ficha(nomeJogador, golsJogador))
