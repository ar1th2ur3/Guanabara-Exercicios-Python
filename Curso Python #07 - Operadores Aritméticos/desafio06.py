def separator():
    print("*" * 50)
separator()
n = int(input("Digite um número, por gentileza:"))
separator()
#Calcule de Dobro:
print("O dobro de {} é: {}".format(n, n*2))
separator()
#Calculo de Triplo:
print("O triplo de {} é: {}".format(n, n*3))
separator()
#Calculo Raiz Quadrada:
print("A raiz quadrada de {} é: {:.0f}".format(n, n**(1/2)))
separator()
print("Finalizado!")
separator()