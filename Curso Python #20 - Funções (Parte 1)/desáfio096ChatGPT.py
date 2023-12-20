# Desafio 096: Faça um programa que tenha uma função chamada área(),
# que receba dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

def linha():
    """Imprime uma linha decorativa."""
    print(50 * "-=")

def calculo_terreno(largura, comprimento):
    """
    Calcula a área de um terreno retangular.

    :param largura: A largura do terreno.
    :param comprimento: O comprimento do terreno.
    :return: A área do terreno.
    """
    terreno = largura * comprimento
    return terreno

# Início do programa principal
print("Controle de Terrenos")
linha()

# Solicita as dimensões do terreno ao usuário
largura = float(input("Qual é a largura do Terreno? "))
comprimento = float(input("Qual é o comprimento do terreno? "))

linha()
print("LARGURA: ", largura)
print("COMPRIMENTO:", comprimento)

# Calcula a área do terreno
terreno_calculo = calculo_terreno(largura, comprimento)

linha()
print(f"A área de um terreno de {largura} x {comprimento} é: {terreno_calculo}.")
