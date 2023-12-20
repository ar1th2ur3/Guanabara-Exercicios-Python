#def separator():
#    print("*" * 25)

#separator()
#nome = str(input("Qual é o seu nome ?"))
#separator()
#print("Olá, {:=^20}! Prazer em te conhecer".format(nome))
#separator()

n1 = int(input("Digite o primeiro número, por gentileza."))
n2 = int(input("Digite o segundo número, por gentileza."))

s = n1 + n2
m = n2 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma é:{} \n O produto é: {} \n A divisão é {:.3f} ".format(s, m, d), end=" ")
print("\n A divisão inteira é:{} \n A potência é:{}".format(di, e))