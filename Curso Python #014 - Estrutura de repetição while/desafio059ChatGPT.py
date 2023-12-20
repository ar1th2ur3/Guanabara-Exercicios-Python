print("Bem-vindo ao Programa de Cálculos")

# Solicita que o usuário insira dois valores
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

while True:
    print("\nOpções disponíveis:")
    print("[1] Somar.")
    print("[2] Multiplicar.")
    print("[3] Encontrar o Maior.")
    print("[4] Inserir Novos Números.")
    print("[5] Sair do Programa.")
    
    # Solicita que o usuário escolha uma opção
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        # Realiza a operação de soma
        soma = v1 + v2
        print(f"A soma de {v1} e {v2} é igual a {soma}.")
    elif opcao == 2:
        # Realiza a operação de multiplicação
        multiplicacao = v1 * v2
        print(f"A multiplicação de {v1} e {v2} é igual a {multiplicacao}.")
    elif opcao == 3:
        # Encontra o maior valor entre os números
        maiorValor = max(v1, v2)
        print(f"O maior valor entre {v1} e {v2} é {maiorValor}.")
    elif opcao == 4:
        # Permite ao usuário inserir novos números
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite o segundo valor: "))
    elif opcao == 5:
        # Sai do programa
        print("Você saiu do programa. Até a próxima!")
        break
    else:
        # Lida com opções inválidas
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")
    
    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja continuar o jogo? (s/n): ").lower()
    if continuar != 's':
        print("Programa encerrado. Obrigado por utilizar nosso serviço!")
        break
