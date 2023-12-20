import datetime

def calculoBissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return f"O ano {ano} é bissexto."
    else:
        return f"O ano {ano} não é bissexto."

def verificaDataBissexto():
    data_atual = datetime.date.today()
    ano_atual = data_atual.year
    mes_atual = data_atual.month
    dia_atual = data_atual.day

    ano_bissexto = calculoBissexto(ano_atual)

    if mes_atual == 2 and dia_atual == 29:
        return f"A data atual ({dia_atual}/{mes_atual}/{ano_atual}) está em um ano bissexto. {ano_bissexto}"
    else:
        return f"A data atual ({dia_atual}/{mes_atual}/{ano_atual}) não está em um ano bissexto. {ano_bissexto}"

def main():
    print("Desafio 032: Faça um programa que verifique se um ano é bissexto e se a data atual está dentro de um ano bissexto.")

    ano = int(input("Digite um ano para verificar se é bissexto ou não: "))
    mensagem_ano = calculoBissexto(ano)
    print(mensagem_ano)

    mensagem_data = verificaDataBissexto()
    print(mensagem_data)

if __name__ == "__main__":
    main()
