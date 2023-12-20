from math import radians, sin, cos, tan

def calculoAngulo(angulo):
    seno = sin(radians(angulo))
    cosseno = cos(radians(angulo))
    tangente = tan(radians(angulo))
    return seno, cosseno, tangente

def main():
    angulo = float(input("Digite o ângulo que você quer: "))

    seno, cosseno, tangente = calculoAngulo(angulo)

    print(f"Seno: {seno:.2f}")
    print(f"Cosseno: {cosseno:.2f}")
    print(f"Tangente: {tangente:.2f}")

if __name__ == "__main__":
    main()
