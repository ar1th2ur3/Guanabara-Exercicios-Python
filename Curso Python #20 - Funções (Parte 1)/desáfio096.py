print("Desáfio 096: Faça um programa que tenha uma função chamda área(), que receba dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.")
def linha():
    print(50 * "-=")

def calculoTerreno(largura,comprimento):
    terreno = largura * comprimento
    return terreno
print("Controle de Terrenos")
linha()
largura = float(input("Qual é a largura do Terreno? "))
comprimento = float(input("Qual é o comprimento do terreno? "))

linha()
print("LARGURA: ", largura)
print("COMPRIMENTO:", comprimento)
terrenoCalculo = calculoTerreno(largura,comprimento)
linha()
print(f"A área de um terreno de {largura} x {comprimento} é: {terrenoCalculo}.")