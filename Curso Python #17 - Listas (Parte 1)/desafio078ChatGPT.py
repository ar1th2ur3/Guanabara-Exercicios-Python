# Desafio 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

# Inicialização da lista vazia
valores = []

# Número de valores a serem lidos
quantidade_valores = 5

# Entrada de dados
for i in range(1, quantidade_valores + 1):
    valor = int(input(f"Digite o {i}º valor: "))
    valores.append(valor)

# Análise dos valores
maior_valor = max(valores)
menor_valor = min(valores)

# Encontrar as posições do maior e menor valores
posicoes_maior = [i for i, v in enumerate(valores) if v == maior_valor]
posicoes_menor = [i for i, v in enumerate(valores) if v == menor_valor]

# Saída de resultados
print(50 * "=")
print(f"Os valores digitados são: {valores}")
print(f"O maior valor digitado é {maior_valor}, nas posições: {posicoes_maior}")
print(f"O menor valor digitado é {menor_valor}, nas posições: {posicoes_menor}")
print(50 * "=")
