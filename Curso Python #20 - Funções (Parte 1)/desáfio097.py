# Desafio 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(texto, texto_contagem):
    """
    Imprime uma mensagem com tamanho adaptável.

    :param texto: O texto a ser exibido.
    :param texto_contagem: O número de vezes que o caractere "~" deve ser repetido.
    """
    print(texto_contagem * "~~")
    print(texto)
    print(texto_contagem * "~~")

# Início do programa principal
print("Controle de Texto")
texto = str(input("Digite um texto: "))

# Calcula a contagem de caracteres no texto
texto_contagem = len(texto)

# Chama a função escreva para exibir o texto com tamanho adaptável
escreva(texto, texto_contagem)
