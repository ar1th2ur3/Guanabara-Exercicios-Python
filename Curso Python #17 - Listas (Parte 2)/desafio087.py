print("Desafio 087: Aprimore o desáfio anterior, mostrando no final:.")
print("A) A soma de todos os valores pares digitados.")
print("B) A soma dos valores da terceira coluna")
print("C) O maior valor da segunda linha.")

# Criando uma matriz vazia 3x3
matriz = [[] for _ in range(3)]
valorTotal = 0
SegundaLinhaMaiorValor = 0
TerceiraLinhaMaiorValor = 0


# Preenchendo a matriz com valores fornecidos pelo usuário
print("\n=== Preenchimento da Matriz ===")

for i in range(3):
    print(f"\nLinha {i+1}:")
    for j in range(3):
        valor = int(input(f"  Digite um número para a posição ({i+1}, {j+1}): "))
        valorTotal += valor
        if i == 2:
            TerceiraLinhaMaiorValor += valor
        matriz[i].append(valor)
    if i == 1:
        #for _ in matriz[i]:
        maxValue = max(matriz[i])
        print(maxValue)

# Imprimindo uma linha para separar a entrada da matriz

print("\n=== Entrada do Usuário e Matriz Resultante ===")
print(50 * "=")

# Exibindo a matriz na tela
for linha in matriz:
    print(linha)

print(f"Total = {valorTotal}")
print(f"Valor total da terceira linha: {TerceiraLinhaMaiorValor}")
print(f"Maior valor da segunda linha: {maxValue}")
# Imprimindo outra linha para separar a matriz da entrada
print(50 * "=")
print("Matriz formatada exibida na tela.")
