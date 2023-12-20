import moeda

print("Desafio 0109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no 0108.")

numero = int(input("Digite um número: "))


print(f"O dobro de {numero} é: {moeda.dobro(numero,formatar=True)}")
print(f"A metade de {numero} é: {moeda.metade(numero,formatar=True)}")
print(f"Aumentando 10%, temos: {moeda.aumentar(numero, 10,formatar=True)}")
print(f"Diminuindo 10%, temos: {moeda.diminuir(numero, 10,formatar=True)}")
