def calculoPares():
    t = 0
    for n in range(0, 6+1):
        if n % 2 == 0:
            print(f" O número: {n} é par, então será somado: {n+1}.")
            t += n + 1
        else: 
            print(f" O número: {n}, é impar, então será desconsiderado.")
    print(f" O total é: {t}")

def main():
    print("Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.")

    calculoPares()

if __name__ == "__main__":
    main()