import math

def calcular_hipotenusa(cateto_oposto, cateto_adjacente):
    hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
    return hipotenusa

def main():
    print("Desafio - 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.")
    
    cateto_oposto = float(input("Comprimento do Cateto Oposto: "))
    cateto_adjacente = float(input("Comprimento do Cateto Adjacente: "))

    hipotenusa = calcular_hipotenusa(cateto_oposto, cateto_adjacente)

    print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")

if __name__ == "__main__":
    main()
