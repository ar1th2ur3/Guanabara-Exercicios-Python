def separator():
    print("*" * 50)

def tabuada(numero, n=10):
    for i in range(1, n + 1):
        resultado = numero * i
        separator()
        print(f"{numero} x {i} = {resultado}")

n = int(input("Quer saber a tabuada de um número? Então digite ele aqui:"))

tabuada(n)
