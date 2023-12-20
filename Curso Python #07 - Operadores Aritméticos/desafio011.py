print("Desafio - 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados")

def calcularArea(l, a):
    area = l * a
    return area

l = float(input("Digite a largura da parede em metros:"))
a = float(input("Digite a altura da parede em metros:"))

area = calcularArea(l, a)

print(f"A área da parede é {area:.1f} metros quadrados")

quantidade_de_tinta = area / 2  # Cada litro de tinta pinta 2 metros quadrados
print(f"A quantidade de tinta necessária será: {quantidade_de_tinta:.1f} litros")
