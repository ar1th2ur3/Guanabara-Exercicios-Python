def main():
    print("Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.")

    for c in range(10,0,-1):
        print(f"Faltam {c} para os fogos começarem!")
    print("Os fogos começaram!")
if __name__ == "__main__":
    main()