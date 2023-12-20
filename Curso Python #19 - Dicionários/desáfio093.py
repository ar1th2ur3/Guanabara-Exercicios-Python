print("Desáfio 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.")
print("O programa vai ler o nome do jogador e quantas partidas ele jogou.")
print("Depois vai ler a quantidade de gols feitos em cada partida.")
print("No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.")

j = {"Gols": [],}
c = list()
somaGols = 0

print(50 * "0-")
j['Nome'] = str(input("Qual é o nome do jogador? "))
print(50 * "0-")
j['Partidas'] = int(input(f"Quantas partidas {j['Nome']} jogou? "))
print(50 * "0-")

for i in range(j["Partidas"]):
    j["Gols"].append(int(input(f"Quantos gols na partida {i+1}? ")))
print(50 * "0-")

for i in j["Gols"]:
    somaGols += i

print("O campo nome tem o valor:", j["Nome"])
print("O campo gols tem o valor:", j["Gols"])
print("O campo total tem o valor:", somaGols)
print(50 * "0-")

print(f"O jogador: {j['Nome']} jogou: {j['Partidas']}.")
for i,k in enumerate(j["Gols"]):
        print(f"Na partid {i+1} ele fez: {k} gols.")
