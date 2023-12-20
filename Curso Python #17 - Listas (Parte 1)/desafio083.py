print("Desáfio 083: Crie um programa onde o usuário digita uma expressão qualquer que use parênteses.")
print("Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.")

lista = []
expressao = str(input("Digite uma expressão, e iremos verificar: "))

for i in expressao:
    if i == "(":
        lista.append("(")
    elif i == ")":
        if len(lista) > 0: 
            lista.pop()
        else:
            lista.append(")")
            break

if len(lista) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está incorreta!")