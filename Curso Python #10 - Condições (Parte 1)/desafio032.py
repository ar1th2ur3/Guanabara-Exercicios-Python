def calculoBissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return f"O ano {ano} é bissexto."
    else:
        return f"O ano {ano} não é bissexto."

def main():
    print("Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.")
    
    ano = int(input("Digite um ano para verificar se é bissexto ou não: "))
    
    mensagem = calculoBissexto(ano)
    
    print(mensagem)

if __name__ == "__main__":
    main()
