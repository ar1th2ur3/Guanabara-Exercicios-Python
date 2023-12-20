print("Desafio 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.")
print("O programa vai ler o nome do jogador e quantas partidas ele jogou.")
print("Depois vai ler a quantidade de gols feitos em cada partida.")
print("No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.")

player_data = {"Gols": []}
total_goals = 0

print(50 * "-")
player_data['Nome'] = str(input("Qual é o nome do jogador? "))
print(50 * "-")
player_data['Partidas'] = int(input(f"Quantas partidas {player_data['Nome']} jogou? "))
print(50 * "-")

for i in range(player_data["Partidas"]):
    player_data["Gols"].append(int(input(f"Quantos gols na partida {i+1}? ")))
print(50 * "-")

total_goals = sum(player_data["Gols"])

print("O campo nome tem o valor:", player_data["Nome"])
print("O campo gols tem o valor:", player_data["Gols"])
print("O campo total tem o valor:", total_goals)
print(50 * "-")

print(f"O jogador: {player_data['Nome']} jogou: {player_data['Partidas']}.")
for i, goals in enumerate(player_data["Gols"], 1):
    print(f"Na partida {i} ele fez: {goals} gols.")
