from random import randint
import time

def calculeKm(vKm):
    vCusto = 0  # Defina um valor padrão para vCusto
    if vKm > 80:
        mensagem = "Você ultrapassou o limite de velocidade."
        vCusto = (vKm - 80) * 7
        mensagem += f" Você será cobrado R${vCusto}."
    else:
        mensagem = "Você não passou do limite de velocidade!"
    return mensagem, vCusto

def main():
    print("Desafio 029: Escreva um programa que leia a velocidade de um carro.")
    time.sleep(2)
    print("Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.")
    time.sleep(2)
    print("A multa vai custar R$7,00 por cada Km acima do limite.")
    time.sleep(2)

    vKm = randint(0, 150)
    
    print("O seu limite de velocidade é:", vKm)
    time.sleep(2)  # Atraso de 2 segundos
    
    mensagem, custo = calculeKm(vKm)
    print(mensagem)
    
    if custo > 0:
        print(f"Total a pagar: R${custo:.2f}")
    
if __name__ == "__main__":
    main()
