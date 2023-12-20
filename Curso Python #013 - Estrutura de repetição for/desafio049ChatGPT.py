def calcular_tabuada(numero):
    tabuada = []

    for i in range(1, 11):
        resultado = numero * i
        tabuada.append((i, resultado))
    
    return tabuada

def exibir_tabuada(tabuada, numero):
    print(f"Tabuada do {numero}:")
    for item in tabuada:
        multiplicador, resultado = item
        print(f"{numero} x {multiplicador} = {resultado}")

def main():
    print("Este programa mostra a tabuada de um número escolhido pelo usuário usando um laço for.")

    try:
        numero = int(input("Digite o número da tabuada que você deseja: "))
        if numero < 1:
            raise ValueError("O número deve ser maior ou igual a 1.")

        tabuada = calcular_tabuada(numero)
        exibir_tabuada(tabuada, numero)

    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
