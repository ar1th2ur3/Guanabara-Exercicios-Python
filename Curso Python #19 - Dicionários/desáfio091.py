from random import randint
from time import sleep

print("Desáfio 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.")
print("Guarde esses resultados em um dicionário.")
print("No final, coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número no dado.")

d = {}
j = []

print('-+' * 50)

for i in range(1, 4 + 1):
    d = {}
    d['jogador'] = i
    d['n'] = randint(0, 6)
    j.append(d.copy())
    print(f"O jogador {d['jogador']} tirou: {d['n']}")
    print("CARREGANDO...")
    sleep(1)

print('-+' * 50)
print("RANKING DOS JOGADORES")
print('-+' * 50)


sorted_j = sorted(j, key=lambda x: x['n'], reverse=True)

for jogador in sorted_j:
    print(f"Jogador {jogador['jogador']} - Pontuação: {jogador['n']}")
    print("CARREGANDO...")
    sleep(1)
