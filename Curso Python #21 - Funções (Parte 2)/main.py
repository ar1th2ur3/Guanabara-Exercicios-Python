def ficha(nome="<desconhecido>", gols=0):
    if not nome.strip():  # Verifica se o nome é vazio ou contém apenas espaços em branco
        nome = "<desconhecido>"
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."

nomeJogador = input("Qual o nome do Jogador? ")
golsJogador = input(f"Quantos gols o jogador {nomeJogador} fez? ")

# Certifique-se de que os gols são um número inteiro
try:
    golsJogador = int(golsJogador)
except ValueError:
    golsJogador = 0

print(ficha(nomeJogador, golsJogador))

