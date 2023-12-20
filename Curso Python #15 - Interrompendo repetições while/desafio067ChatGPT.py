def tabuada():
    try:
        while True:
            # Solicita o número desejado para a tabuada
            n = int(input("Digite o número desejado para a tabuada (ou um número negativo para encerrar): "))

            # Verifica se o usuário deseja encerrar a tabuada
            if n < 0:
                break

            # Mostra a tabuada do número fornecido
            print(f"\nTabuada do {n}:")
            for t in range(1, 10):
                resultado = n * t
                print(f"{n} x {t} = {resultado}")

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

if __name__ == "__main__":
    print("Programa da Tabuada")
    tabuada()
    print("Programa encerrado.")
