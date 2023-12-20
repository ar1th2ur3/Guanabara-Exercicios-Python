def main():
    try:
        numeros_digitados = 0
        soma = 0

        while True:
            entrada = input("Digite um número (ou 999 para parar): ")

            # Verifica se o usuário deseja encerrar a entrada de números
            if entrada == '999':
                break

            # Converte a entrada para um número inteiro
            numero = int(entrada)

            # Incrementa o contador de números digitados e atualiza a soma
            numeros_digitados += 1
            soma += numero

        # Exibe os resultados ao usuário
        print("\nResumo:")
        print(f"Números digitados: {numeros_digitados}")
        print(f"Soma dos números: {soma}")

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    main()
