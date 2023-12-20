# Desafio 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(texto, caractere="~"):
    """
    Imprime uma mensagem com tamanho adaptável, utilizando um caractere específico.

    :param texto: O texto a ser exibido.
    :param caractere: O caractere a ser repetido para formar a borda. Padrão é "~".
    """
    tamanho_borda = 4
    texto_formatado = f"{caractere * tamanho_borda} {texto} {caractere * tamanho_borda}"
    
    print(caractere * len(texto_formatado))
    print(texto_formatado)
    print(caractere * len(texto_formatado))

# Início do programa principal
print("Controle de Texto")

try:
    texto = str(input("Digite um texto: "))

    if not texto.strip():
        raise ValueError("O texto não pode ser vazio.")

    caractere_borda = input("Digite o caractere para a borda (padrão é '~'): ") or "~"

    # Chama a função escreva para exibir o texto com tamanho adaptável
    escreva(texto, caractere_borda)

except ValueError as ve:
    print(f"Erro: {ve}")

except Exception as e:
    print(f"Erro inesperado: {e}")
