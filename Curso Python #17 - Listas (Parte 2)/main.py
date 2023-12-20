pessoas = []
dados = []

for c in range(2):
    dados.append(str(input("Qual é o nome?")))
    dados.append(str(input("Qual é a idade?")))
    pessoas.append(dados[:])
    dados.clear()

print("A lista de dados é:", dados)
print("A lista de pessoas é:", pessoas)
    

