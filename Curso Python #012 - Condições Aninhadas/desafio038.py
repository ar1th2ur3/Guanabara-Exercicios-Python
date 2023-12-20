from random import randint

def verificaçãoMaior(n1,n2):
    if n1 > n2:
       return f"O primeiro número: {n1} é maior que o segundo número: {n2}"
    elif n2 > n1:
        return f"O segundo número: {n2} é maior que o primeiro número: {n1}"
    else:
        return f"O primeiro número: {n1} e o segundo número {n2} são iguais."

def main():
    n1 = randint(1, 10)
    n2 = randint(1, 10)

    message = verificaçãoMaior(n1,n2)

    print(message)

if __name__ == "__main__":
    main()