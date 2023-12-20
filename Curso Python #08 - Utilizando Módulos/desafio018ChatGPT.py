import math

def calcularFuncoesTrigonometricas(angulo):
    seno = math.sin(angulo)
    cos = math.cos(angulo)
    tan = math.tan(angulo)
    return seno, cos, tan

def main():
    print("Desafio - Cálculo de Funções Trigonométricas")
    
    angulo = float(input("Digite o ângulo (em radianos): "))

    seno, cos, tan = calcularFuncoesTrigonometricas(angulo)

    print(f"Ângulo em radianos: {angulo:.2f}")
    print(f"Seno: {seno:.2f}")
    print(f"Cosseno: {cos:.2f}")
    print(f"Tangente: {tan:.2f}")

if __name__ == "__main__":
    main()
