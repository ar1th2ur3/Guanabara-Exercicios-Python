def separator():
    print("*" * 50)
separator()
n = int(input("Digite um número, por gentileza."))
print("O número que você escolheu foi:{0}. \n O sucessor desse número é:{1}. \n O antecessor desse número é:{2}.".format(n, n+1, n-1))
separator()