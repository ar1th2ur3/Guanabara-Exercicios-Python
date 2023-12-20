# Desafio - 011: Programa para calcular a quantidade de tinta necessária para pintar uma parede

def calcular_area_parede(largura, altura):
    area = largura * altura
    return area

def calcular_quantidade_tinta(area_parede):
    litros_por_metro_quadrado = 2
    quantidade_tinta = area_parede / litros_por_metro_quadrado
    return quantidade_tinta

def main():
    print("Desafio - 011: Calculadora de tinta para pintar uma parede")
    
    largura = float(input("Digite a largura da parede em metros: "))
    altura = float(input("Digite a altura da parede em metros: "))
    
    area_parede = calcular_area_parede(largura, altura)
    quantidade_tinta = calcular_quantidade_tinta(area_parede)
    
    print(f"A área da parede é {area_parede:.1f} metros quadrados.")
    print(f"A quantidade de tinta necessária será: {quantidade_tinta:.1f} litros.")

if __name__ == "__main":
    main()
