print("Crie um programa que leia dois valores e mostre um menu na tela.")
print("[1] Somar.")
print("[2] Multiplicar.")
print("[3] Maior.")
print("[4] Novos números.")
print("[5] Sair do programa.")

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

while True:
    print("\nSelecione uma das opções abaixo: ")
    print("[1] Somar.")
    print("[2] Multiplicar.")
    print("[3] Maior.")
    print("[4] Novos números.")
    print("[5] Sair do programa.")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        soma = v1 + v2
        print(f"A soma de {v1} e {v2} é igual a {soma}.")
        continuar = input("Deseja continuar o jogo? (s/n): ").lower()
        if continuar != 's':
            break
    elif opcao == 2:
        multiplicacao = v1 * v2
        print(f"A multiplicação de {v1} e {v2} é igual a {multiplicacao}.")
        continuar = input("Deseja continuar o jogo? (s/n): ").lower()
        if continuar != 's':
            break
    elif opcao == 3:
        maiorValor = max(v1, v2)
        print(f"O maior valor entre {v1} e {v2} é {maiorValor}.")
        continuar = input("Deseja continuar o jogo? (s/n): ").lower()
        if continuar != 's':
            break
    elif opcao == 4:
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Você saiu do programa.")
        break
    else:
        print("Opção inválida. Selecione uma opção de 1 a 5.")
