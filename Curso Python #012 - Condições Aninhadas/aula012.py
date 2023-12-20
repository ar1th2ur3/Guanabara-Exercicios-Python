def verificacaoNome(nome):
    if nome == "Arthur":
        print("Nossa, que nome bonito.")
    elif nome == "ARTHUR" or nome == "Lucas":
        print("pq vc esta gritando ?")
    else:
        print("Nossa, que nome feio.")
    return nome

nome = str(input("Qual é o seu nome? "))

message = verificacaoNome(nome)

print(message)