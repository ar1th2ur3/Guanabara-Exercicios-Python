from random import randint
import time

def calculeKm(vKm):
    vCusto = max(0, (vKm - 80) * 7)
    mensagem = "Você ultrapassou o limite de velocidade." if vCusto > 0 else "Você não passou do limite de velocidade."
    return mensagem, vCusto

def main():
    print("Desafio 029: Escreva um programa que leia a velocidade de um carro.")
    print("Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.")
    print("A multa vai custar R$7,00 por cada Km acima do limite.")

    vKm = randint(0, 150)
    print(f"O seu limite de velocidade é: {vKm}")
    
    time.sleep(2)  # Atraso de 2 segundos
    mensagem, custo = calculeKm(vKm)
    print(mensagem)
    
    if custo > 0:
        print(f"Total a pagar: R${custo:.2f}")
    
if __name__ == "__main__":
    main()
