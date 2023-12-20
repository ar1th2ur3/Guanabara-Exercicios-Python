print("Desáfio 080: Crie um programa onde o usuário possa digitar cinco valores núméricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sorte)")
print(50 * "=")
print("No final, mostre a lista ordenada na tela.")
print(50 * "=")

l = []

for rodada in range(1, 6):
    print(f"\n======= Rodada {rodada} =======")
    
    while True:
        try:
            numero = int(input(f"Digite o valor desejado para a rodada {rodada}: "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    
    inserido = False

    print(f"\nVocê digitou o número: {numero}")

    for chave, valor in enumerate(l):
        print(f"Comparando {numero} com {valor} na posição {chave + 1} da lista...")

        if numero < valor:
            print(f"{numero} é menor do que {valor}. Inserindo {numero} na posição {chave + 1} da lista.")
            l.insert(chave, numero)
            inserido = True
            break

    if not inserido:
        print(f"{numero} é maior do que todos os números existentes. Adicionando ao final da lista.")
        l.append(numero)

    print(f"Lista Atual: {l}")

print("\nJogo completo! Aqui está a lista final organizada:", l)


