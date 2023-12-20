c = 5

l = []
for v in range (0,c):
    l.append(int(input("Digite um valor")))


print(l)

for p, v in enumerate(l):

    print(f"Na posição {p} tem o valor: {v}")