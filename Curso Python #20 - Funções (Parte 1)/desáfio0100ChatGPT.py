from random import randint

def sorteia() -> list:
    """Função para sortear 5 números inteiros entre 0 e 10 e colocá-los em uma lista."""
    numeros = [randint(0, 10) for _ in range(5)]
    print(f"Sorteando 5 valores da lista: {numeros} PRONTO!")
    return numeros

def soma_par(lista: list) -> int:
    """Função para calcular a soma dos valores pares em uma lista."""
    valores_pares = [i for i in lista if i % 2 == 0]
    soma = sum(valores_pares)
    print(f"Somando os valores pares de {lista}, temos: {soma}")
    return soma

def encontra_maior(lista: list) -> int:
    """Função para encontrar o maior valor em uma lista."""
    maior_valor = max(lista)
    print(f"O maior valor na lista é: {maior_valor}")
    return maior_valor

# Interagindo com o usuário
print("Desafio 0100: Faça um programa que tenha uma lista chamada 'numeros' e duas funções chamadas 'sorteia()' e 'soma_par()'.")
print("A primeira função vai sortear 5 números inteiros entre 0 e 10 e vai colocá-los dentro da lista.")
print("A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.")

try:
    # Executando as funções
    numeros_sorteado = sorteia()
    soma_pares = soma_par(numeros_sorteado)

    # Exibindo o maior valor sorteado
    maior_valor = encontra_maior(numeros_sorteado)
    print(f"O maior valor sorteado foi: {maior_valor}")

    # Testando as funções
    print("\nTestando sorteia():")
    sorteia()

    print("\nTestando soma_par():")
    soma_par(numeros_sorteado)

except Exception as e:
    print(f"Ocorreu um erro: {e}")
