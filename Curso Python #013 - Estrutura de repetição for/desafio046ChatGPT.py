import time

def contagem_regressiva(segundos):
    for c in range(segundos, 0, -1):
        print(f"Faltam {c} segundos para os fogos começarem!")
        time.sleep(1)

def iniciar_fogos():
    print("Os fogos começaram!")

def main():
    print("Este programa mostra uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.")
    
    contagem_regressiva(10)
    iniciar_fogos()

if __name__ == "__main__":
    main()
