
def calculoPar(intervalo):
    for c in range(0, intervalo):
        if c % 2 == 0:
            print(c)
            
def main():
    print("Crie um programa que mostre na tela todos os numeres pares que estão no intervalo entre 1 e 50.")

    calculoPar(100)

if __name__ == "__main__":
    main()