from math import hypot

def calculoHipotenusa(co, ca):
    hi = hypot(co, ca)
    return hi

def main():
    print("Desafio - 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.")
    
    co = float(input("Comprimento do Cateto Oposto: "))
    ca = float(input("Comprimento do Cateto Adjacente: "))

    hi = calculoHipotenusa(co, ca)

    print(f"A hipotenusa é: {hi:.2f}")

if __name__ == "__main__":
    main()
