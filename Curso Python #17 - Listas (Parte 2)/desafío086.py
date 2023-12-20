print("Desafio 086: Crie um programa que crie uma matriz de dimensão 3x3.")
print("Preencha com valores lidos pelo teclado.")
print("No final, mostre a matriz na tela, com a formatação correta.")

# Criando uma matriz vazia 3x3
matriz = [[] for _ in range(3)]

# Preenchendo a matriz com valores fornecidos pelo usuário
print("\n=== Preenchimento da Matriz ===")
for i in range(3):
    print(f"\nLinha {i+1}:")
    for j in range(3):
        valor = int(input(f"  Digite um número para a posição ({i+1}, {j+1}): "))
        print(f"Adicionando o valor {valor} à posição ({i+1}, {j+1}) da matriz.")
        matriz[i].append(valor)

# Imprimindo uma linha para separar a entrada da matriz
print("\n=== Entrada do Usuário e Matriz Resultante ===")
print(50 * "=")

# Exibindo a matriz na tela
for linha in matriz:
    print(linha)

# Imprimindo outra linha para separar a matriz da entrada
print(50 * "=")
print("Matriz formatada exibida na tela.")
