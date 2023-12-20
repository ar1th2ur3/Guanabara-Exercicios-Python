from random import randint
from time import sleep

print("Desáfio 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites")
print("O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta")


jogos = []

n = int(input("Quantos jogos você quer que eu sorteie ? "))

print(f"=== SORTEANDO {n} JOGOS ===")

for i in range(n):
    jogos.clear()
    print("GERANDO OS JOGOS...")
    sleep(1)
    
    for _ in range(6):
        v = randint(0,5000)
        jogos.append(v)
      
    print(f"Jogo {i+1}:{jogos}")
   

        
